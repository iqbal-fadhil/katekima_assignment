from rest_framework import generics
from .models_sell import SellHeader, SellDetail
from .serializers_sell import SellHeaderSerializer, SellDetailSerializer

# This is the List and Create view for Sale
class SellHeaderListCreateView(generics.ListCreateAPIView):
    queryset = SellHeader.objects.filter(is_deleted=False)
    serializer_class = SellHeaderSerializer

# This is the Detail view for Sale Header
class SellHeaderDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'code'
    serializer_class = SellHeaderSerializer

    def get_queryset(self):
        return SellHeader.objects.filter(is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

# This is the List and Create view for Sale Detail
class SellDetailListCreateView(generics.ListCreateAPIView):
    serializer_class = SellDetailSerializer

    def get_queryset(self):
        header_code = self.kwargs['header_code']
        return SellDetail.objects.filter(header__code=header_code, header__is_deleted=False)

    def perform_create(self, serializer):
        header_code = self.kwargs['header_code']
        header = SellHeader.objects.get(code=header_code, is_deleted=False)
        serializer.save(header=header)