from django import forms
from .models import Topping

class TableNoForm(forms.Form):
    '''テーブル番号入力フォーム'''
    table_no = forms.IntegerField(
        label='テーブル番号', min_value=1, max_value=10,
        widget=forms.Select(choices=[(i, i) for i in range(1, 11)]))

class SelectItemForm(forms.Form):
    '''商品選択フォーム'''
    item_id = forms.IntegerField(widget=forms.HiddenInput())

class ToppingOrderForm(forms.Form):
    '''トッピングと数量を入力するフォーム'''
    topping = forms.ModelChoiceField(queryset=Topping.objects.all(), label='トッピング')
    quantity = forms.ChoiceField(
        choices=[('', '---------')] + [(i, i) for i in range(1, 6)],
        label='数量'
    )

# トッピングと数量を複数入力するフォーム
ToppingOrderFormSet = forms.formset_factory(ToppingOrderForm, extra=3)

class ConfirmForm(forms.Form):
    '''注文確認フォーム'''
    is_ok = forms.BooleanField(widget=forms.HiddenInput(), required=True, initial=True)