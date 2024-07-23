from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .models import Item, Topping, Order, ToppingOrder
from . import forms
from . import session


def index(request):
    '''セルフオーダーのトップページ'''
    form = forms.TableNoForm(request.POST or None)
    if form.is_valid():
        table_no = form.cleaned_data['table_no']
        # セッションデータ作成
        session_order = session.SessionOrder(table_no=table_no)
        request.session['session_order'] = session_order.as_dict()
        # メニューページへリダイレクトする
        return redirect('menu')
    return render(request, 'index.html', {'form': form})


class MenuView(TemplateView):
    '''メニューページ'''
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = Item.objects.all()
        context['item_and_forms'] = [(item, forms.SelectItemForm(initial={'item_id': item.id})) for item in items]
        return context

    def post(self, request, *args, **kwargs):
        '''注文ボタンが押されたときの処理'''
        item_id = int(request.POST['item_id'])
        # セッションデータ取得
        session_order = session.SessionOrder.from_dict(request.session['session_order'])
        session_order.item_id = item_id
        # セッションデータを更新
        request.session['session_order'] = session_order.as_dict()
        # トッピング選択へリダイレクト
        return redirect('select_topping')


class SelectToppingView(FormView):
    '''トッピング選択ページ'''
    template_name = 'select_topping.html'
    form_class = forms.ToppingOrderFormSet
    success_url = reverse_lazy('confirm')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # セッションデータ取得
        session_order = session.SessionOrder.from_dict(self.request.session['session_order'])
        # セッションに保存されているトッピングをフォームにセット
        kwargs['initial'] = [{'topping': t.topping_id, 'quantity': t.quantity} for t in session_order.toppings]
        return kwargs

    def form_valid(self, form):
        # セッションデータ取得
        session_order = session.SessionOrder.from_dict(self.request.session['session_order'])
        # トッピングをセット
        for form_part in form.forms:
            if form_part.cleaned_data:
                session_order.toppings.append(session.SessionToppingOrder(topping_id=form_part.cleaned_data['topping'].id, quantity=form_part.cleaned_data['quantity']))
        # セッションデータを更新
        self.request.session['session_order'] = session_order.as_dict()
        return super().form_valid(form)


class ConfirmView(FormView):
    '''注文確認ページ'''
    template_name = 'confirm.html'
    form_class = forms.ConfirmForm
    success_url = reverse_lazy('complete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # セッションデータ取得
        session_order = session.SessionOrder.from_dict(self.request.session['session_order'])
        context['session_order'] = session_order
        context['item'] = Item.objects.get(pk=session_order.item_id)
        context['topping_and_quantities'] = [(Topping.objects.get(pk=t.topping_id), t.quantity) for t in session_order.toppings]
        return context

    def form_valid(self, form):
        # セッションデータ取得
        session_order = session.SessionOrder.from_dict(self.request.session['session_order'])
        # 注文データを作成
        order = Order.objects.create(
            table_no=session_order.table_no,
            item_id=session_order.item_id,
        )
        # トッピング注文データを作成
        for topping in session_order.toppings:
            ToppingOrder.objects.create(
                order=order,
                topping_id=topping.topping_id,
                quantity=topping.quantity,
            )
        # セッションデータを更新
        session_order.is_ordered = True
        self.request.session['session_order'] = session_order.as_dict()
        return super().form_valid(form)


class CompleteView(TemplateView):
    '''注文完了ページ'''
    template_name = 'complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # セッションデータ取得
        session_order = session.SessionOrder.from_dict(self.request.session['session_order'])
        context['session_order'] = session_order
        return context