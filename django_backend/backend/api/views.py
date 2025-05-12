from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    
    def get_queryset(self):
        if self.request.user.role == 'marketing':
            return Lead.objects.filter(generated_by__area=self.request.user.area)
        elif self.request.user.role == 'lead':
            return Lead.objects.filter(generated_by=self.request.user)
        return Lead.objects.all()

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    
    @action(detail=True, methods=['post'])
    def scan(self, request, pk=None):
        coupon = self.get_object()
        if coupon.is_active and coupon.is_valid():
            # Process coupon scanning
            return Response({'status': 'success'})
        return Response({'status': 'invalid'}, status=400)

class FranchiseViewSet(viewsets.ModelViewSet):
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer
    
    @action(detail=True, methods=['get'])
    def dashboard(self, request, pk=None):
        franchise = self.get_object()
        leads = Lead.objects.filter(location=franchise.address)
        sales = Sale.objects.filter(franchise=franchise)
        return Response({
            'lead_count': leads.count(),
            'sales_total': sum(sale.amount for sale in sales),
            'staff_count': User.objects.filter(franchise=franchise).count()
        })