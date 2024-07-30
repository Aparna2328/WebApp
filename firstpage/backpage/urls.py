from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('func/',views.func,name='func'),
    path('products/',views.products,name='products'),
    path('account/',views.account,name='account'),

] 