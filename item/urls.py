from django.urls import path, include
from . import views

app_name = "item"
urlpatterns = [
    path('<int:pk>/', views.item_detail, name='item-detail'),
    path('edit-item/<int:pk>', views.editItem, name='edit-item'),
    path('delete-item/<int:pk>', views.deleteItem, name='delete-item'),
]
