from django.shortcuts import render
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
        # TODO: メニューページへリダイレクトする
    return render(request, 'index.html', {'form': form})