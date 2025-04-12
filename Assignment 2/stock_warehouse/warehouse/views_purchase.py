from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models_purchase import PurchaseHeader, PurchaseDetail
from .models_item import Item
from .serializers_purchase import PurchaseHeaderSerializer, PurchaseDetailSerializer

class PurchaseHeaderListCreateView(APIView):
    def get(self, request):
        headers = PurchaseHeader.objects.filter(is_deleted=False)
        serializer = PurchaseHeaderSerializer(headers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseHeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseHeaderDetailView(APIView):
    def get_object(self, code):
        return get_object_or_404(PurchaseHeader, code=code, is_deleted=False)

    def get(self, request, code):
        header = self.get_object(code)
        serializer = PurchaseHeaderSerializer(header)
        return Response(serializer.data)

    def put(self, request, code):
        header = self.get_object(code)
        serializer = PurchaseHeaderSerializer(header, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code):
        header = self.get_object(code)
        header.is_deleted = True
        header.save()
        return Response({'detail': f'Purchase {code} soft-deleted.'}, status=status.HTTP_204_NO_CONTENT)

class PurchaseDetailListCreateView(APIView):
    def get(self, request, header_code):
        header = get_object_or_404(PurchaseHeader, code=header_code, is_deleted=False)
        details = PurchaseDetail.objects.filter(header=header)
        data = [{
            "item_code": d.item.code,
            "quantity": d.quantity,
            "unit_price": d.unit_price,
            "header_code": d.header.code
        } for d in details]
        return Response(data)

    def post(self, request, header_code):
        data = request.data
        data['header_code'] = header_code
        serializer = PurchaseDetailSerializer(data=data)
        if serializer.is_valid():
            detail = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
