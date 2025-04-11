from django.urls import path
from .views_item import ItemListCreateView, ItemDetailView

urlpatterns = [
    # Items
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<str:code>/', ItemDetailView.as_view(), name='item-detail'),
]
