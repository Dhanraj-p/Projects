from django.contrib import admin
from django.urls import path,include
from ecom import views

urlpatterns = [
    path('',views.home),
    path('employee',views.sdta),
    path('storedata',views.store),
    path('eview',views.eview),
    path('updateemp/<int:ud>',views.upd),
    path('selectemp/<int:st>',views.slt),
    path('deleteemp/<int:de>',views.delet),
    path('change',views.change),
    path('ordernew',views.ordernew),
    path('order',views.new),
    path('orderview',views.orderview),
]