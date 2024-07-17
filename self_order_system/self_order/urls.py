from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('menu/', views.menu, name='menu'),
    # path('order/', views.order, name='order'),
    # path('order/confirm/', views.order_confirm, name='order_confirm'),
    # path('order/complete/', views.order_complete, name='order_complete'),
]
