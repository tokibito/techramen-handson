from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # トップ画面
    path('menu/', views.MenuView.as_view(), name='menu'),  # メニュー画面
    path('select_topping/', views.SelectToppingView.as_view(), name='select_topping'),  # トッピング選択画面
    path('confirm/', views.ConfirmView.as_view(), name='confirm'),  # 確認画面
    path('complete/', views.CompleteView.as_view(), name='complete'),  # 完了画面
]