from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models_item import Item
from .models_purchase import PurchaseHeader, PurchaseDetail
from .models_sell import SellHeader, SellDetail

class StockReportView(APIView):
    def get(self, request, item_code):
        start_date_str = request.GET.get("start_date")
        end_date_str = request.GET.get("end_date")

        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required."}, status=400)

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except ValueError:
            return Response({"error": "Invalid date format, use YYYY-MM-DD."}, status=400)

        item = get_object_or_404(Item, code=item_code, is_deleted=False)

        purchases = PurchaseDetail.objects.filter(
            item=item,
            header__date__range=(start_date, end_date),
            is_deleted=False,
            header__is_deleted=False
        ).select_related('header')

        sells = SellDetail.objects.filter(
            item=item,
            header__date__range=(start_date, end_date),
            is_deleted=False,
            header__is_deleted=False
        ).select_related('header')

        combined = []
        for p in purchases:
            combined.append({
                "date": p.header.date,
                "description": p.header.description,
                "code": p.header.code,
                "in_qty": p.quantity,
                "in_price": p.unit_price,
                "in_total": p.quantity * p.unit_price,
                "out_qty": 0,
                "out_price": 0,
                "out_total": 0,
            })

        for s in sells:
            avg_price = item.balance / item.stock if item.stock > 0 else 0
            combined.append({
                "date": s.header.date,
                "description": s.header.description,
                "code": s.header.code,
                "in_qty": 0,
                "in_price": 0,
                "in_total": 0,
                "out_qty": s.quantity,
                "out_price": avg_price,
                "out_total": avg_price * s.quantity,
            })

        combined.sort(key=lambda x: x['date'])

        stock_qty = []
        stock_price = []
        stock_total = []
        balance_qty = 0
        balance = 0
        result_items = []

        for entry in combined:
            if entry['in_qty'] > 0:
                stock_qty.append(entry['in_qty'])
                stock_price.append(entry['in_price'])
                stock_total.append(entry['in_total'])
            elif entry['out_qty'] > 0:
                out_qty = entry['out_qty']
                total_out = 0
                for i in range(len(stock_qty)):
                    if out_qty == 0:
                        break
                    available = stock_qty[i]
                    if available == 0:
                        continue
                    use = min(available, out_qty)
                    stock_qty[i] -= use
                    total_out += use * stock_price[i]
                    out_qty -= use
                entry['out_total'] = total_out
                entry['out_price'] = total_out / entry['out_qty'] if entry['out_qty'] else 0

            entry['stock_qty'] = stock_qty.copy()
            entry['stock_price'] = stock_price.copy()
            entry['stock_total'] = [q * p for q, p in zip(stock_qty, stock_price)]
            entry['balance_qty'] = sum(stock_qty)
            entry['balance'] = sum(entry['stock_total'])

            balance_qty = entry['balance_qty']
            balance = entry['balance']

            entry['date'] = entry['date'].strftime('%d-%m-%Y')
            result_items.append(entry)

        summary = {
            "in_qty": sum(i["in_qty"] for i in result_items),
            "out_qty": sum(i["out_qty"] for i in result_items),
            "balance_qty": balance_qty,
            "balance": balance
        }

        return Response({
            "result": {
                "items": result_items,
                "item_code": item.code,
                "name": item.name,
                "unit": item.unit,
                "summary": summary
            }
        })