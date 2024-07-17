from django import forms


class TableNoForm(forms.Form):
    '''テーブル番号入力フォーム'''
    table_no = forms.IntegerField(
        label='テーブル番号', min_value=1, max_value=10,
        widget=forms.Select(choices=[(i, i) for i in range(1, 11)]))