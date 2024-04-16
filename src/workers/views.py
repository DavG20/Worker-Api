from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from src.workers.models import Unit, Visit, Worker
from src.workers.serializers import CreateUnitSerializer, CreateVisitSerializer, UnitSerializer, VisitSerializer, WorkerSerializer
from datetime import datetime
import pytz
# Create your views here.


class WorkerViewSet(viewsets.ViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def list(self, request):
        serializer = WorkerSerializer(self.queryset, many=True)
        return Response({'success': True, "data": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        worker = Worker.objects.filter(id=pk).first()
        if worker:
            serializer = WorkerSerializer(worker)
            return Response({'success': True, "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'No worker found with the provided ID'}, status=status.HTTP_404_NOT_FOUND)



class UnitViewSet(viewsets.ViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def list(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"success": False, 'message': 'phone number is required to fetch specific list unit'}, status=status.HTTP_400_BAD_REQUEST)
        # filter list of unit  linked to specified worker
        self.queryset = self.queryset.filter(worker__phone_number=phone_number)
        serializer = UnitSerializer(self.queryset, many=True)
        return Response({'success': True, "data": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        unit = Unit.objects.filter(id=pk).first()
        if unit:
            serializer = UnitSerializer(unit)
            return Response({'success': True, "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'No unit found with the provided ID'}, status=status.HTTP_404_NOT_FOUND)



class VisitViewSet(viewsets.ViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    
    def create(self, request):
        unit_pk = request.data.get('unit')
        latitude= request.data.get('latitude')
        longitude= request.data.get('longitude')
        if not latitude or not longitude:
            return Response({"success": False, 'message': 'latitude or longitude is required '}, status=status.HTTP_400_BAD_REQUEST)
        if not unit_pk:
            return Response({"success": False, 'message': 'unit pk  is required '}, status=status.HTTP_400_BAD_REQUEST)
            
        data = request.data
        
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"success": False, 'message': 'phone number is required '}, status=status.HTTP_400_BAD_REQUEST)
        
        unit = Unit.objects.filter(pk=unit_pk).first()
        if not unit :
            return Response({'success': False, 'message': 'No unit found with the provided ID'}, status=status.HTTP_404_NOT_FOUND)
            
        if unit.worker.phone_number  != phone_number:
            return Response({'success': False, 'message': 'No units found with the provided phone number and unit id '}, status=status.HTTP_403_FORBIDDEN)
        
        data['visit_date'] = pytz.UTC.localize(datetime.today())
        
        serializer = CreateVisitSerializer(data=request.data, read_only=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        visit = Unit.objects.filter(id=pk).first()
        serializer = CreateVisitSerializer(visit, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, "data": serializer.data}, status=status.HTTP_200_OK)

    