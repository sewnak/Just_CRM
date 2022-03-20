"""Just_CRM1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from CRM import views
from CRM.views import DeleteCustomerView, DeleteOfferView, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.Index.as_view(), name='index'),
    path('customers/', views.CustomerView.as_view(), name='customers'),
    path('customers/delete/<int:customer_id>/', DeleteCustomerView.as_view(), name="delete_customer"),
    path('add_customer/', views.AddCustomer.as_view(), name='add_customer'),
    path('edit_customer/<int:customer_id>/', views.EditCustomerView.as_view(), name='edit_customer'),
    path('offers/', views.OfferView.as_view(), name='offers'),
    path('offers/delete/<int:offer_id>/', DeleteOfferView.as_view(), name="delete_offer"),
    path('add_offer/', views.AddOffer.as_view(), name='add_offer'),
    path('contracts/', views.ContractView.as_view(), name='contracts'),
    path('add_contract/', views.AddContract.as_view(), name='add_contract'),
    path('invests/', views.InvestView.as_view(), name='invests'),
    path('add_invest/', views.AddInvest.as_view(), name='add_invest'),
    path('apartments/', views.ApartmentView.as_view(), name='apartments'),
    path('add_apartment/', views.AddApartment.as_view(), name='add_apartment'),
]
