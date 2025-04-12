from django.urls import path
from .views_item import ItemListCreateView, ItemDetailView
from .views_purchase import (
    PurchaseHeaderListCreateView,
    PurchaseHeaderDetailView,
    PurchaseDetailListCreateView,
)


urlpatterns = [
    # Items
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<str:code>/', ItemDetailView.as_view(), name='item-detail'),

    # Purchases
    path('purchase/', PurchaseHeaderListCreateView.as_view(), name='purchase-list'),
    path('purchase/<str:code>/', PurchaseHeaderDetailView.as_view(), name='purchase-detail'),
    path('purchase/<str:header_code>/details/', PurchaseDetailListCreateView.as_view(), name='purchase-details'),    
]
