from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('paycheck', views.paycheck),
    path('paycheck/checkout/<int:order_id>', views.checkout)
]
