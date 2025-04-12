from django.urls import path
from .views_item import (
    ItemListCreateView, 
    ItemDetailView,
)
from .views_purchase import (
    PurchaseHeaderListCreateView,
    PurchaseHeaderDetailView,
    PurchaseDetailListCreateView,
)
from .views_sell import (
    SellHeaderListCreateView, 
    SellHeaderDetailView, 
    SellDetailListCreateView
)


urlpatterns = [
    # Items
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<str:code>/', ItemDetailView.as_view(), name='item-detail'),

    # Purchases
    path('purchase/', PurchaseHeaderListCreateView.as_view(), name='purchase-list'),
    path('purchase/<str:code>/', PurchaseHeaderDetailView.as_view(), name='purchase-detail'),
    path('purchase/<str:header_code>/details/', PurchaseDetailListCreateView.as_view(), name='purchase-details'),   

    # Sales
    path('sell/', SellHeaderListCreateView.as_view(), name='sell-list-create'),
    path('sell/<str:code>/', SellHeaderDetailView.as_view(), name='sell-detail'),
    path('sell/<str:header_code>/details/', SellDetailListCreateView.as_view(), name='sell-details'),     
]
