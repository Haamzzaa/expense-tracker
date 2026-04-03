from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_expense, name='add_expense'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
    path('api/expenses/', views.expense_list, name='expense-list'),
    path('api/expenses/<int:id>/', views.expense_detail, name='expense-detail'),
]