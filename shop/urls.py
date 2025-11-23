from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('createaccount', views.createaccount, name='createaccount'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('customer_details', views.customer_details, name='customer_details'),
    path('delete/<str:accnumber>/', views.delete_customer, name='delete_customer'),
    path('edit_customer/<str:accnumber>/', views.edit_customer, name='edit_customer'),

]