from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('select_topping/', views.SelectToppingView.as_view(), name='select_topping'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm'),
    path('complete/', views.CompleteView.as_view(), name='complete'),
]
