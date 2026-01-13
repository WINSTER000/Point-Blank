from django.urls import path
from django.contrib import admin
from .views import Client

clients = Client()

urlpatterns = [
    path('contact',clients.contact),
    path('contact_info',clients.contact_info),
    path('login',clients.login),
    path('register',clients.register),
    path('client_login',clients.client_login),
    path('client_register',clients.client_register),
    path('add_to_cart',clients.add_to_cart),
    path('remove_from_cart',clients.remove_from_cart),
    path('create_order',clients.create_order),
    path('cart',clients.cart),
    path('profile',clients.profile),
    path('delete_account',clients.delete_account),
    path('delete_account',clients.delete_account),
    path('success',clients.success),
    path('failure',clients.failure),
    path('logout',clients.logout),
    path('404',clients.error_404),
]