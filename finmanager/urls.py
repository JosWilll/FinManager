from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("transactions", views.transactions, name="transactions"),
    path("transactions/new", views.transCreate, name="transCreate"),
    path("transactions/edit/<int:pk>/", views.transEdit, name="transEdit"),
    path("transactions/delete/<int:pk>", views.transDelete, name="transDelete"),

    path("categories", views.categories, name="categories"),
    path("categories/new", views.catCreate, name="catCreate"),
    path("categories/edit/<int:pk>/", views.catEdit, name="catEdit"),
    path("categories/delete/<int:pk>", views.catDelete, name="catDelete"),

    path("accounts", views.accounts, name="accounts"),
    path("accounts/new", views.accCreate, name="accCreate"),
    path("accounts/edit/<int:pk>/", views.accEdit, name="accEdit"),
    path("accounts/delete/<int:pk>", views.accDelete, name="accDelete"),
]
