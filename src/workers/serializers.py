from dataclasses import fields
from urllib import request
from rest_framework import serializers

from src.workers.models import Unit, Visit, Worker



class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('name' ,"phone_number" )
        
    
class CreateWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"
    def create(self, validated_data):
        worker = Worker.objects.create(**validated_data)
        return worker

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.phone_number = validated_data.get('phone_number' , str(instance.phone_number))
        
        instance.save()
        return instance
    
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('pk' ,"name" )
        
    
class CreateUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"
    def create(self, validated_data):
        unit = Unit.objects.create(**validated_data)
        return unit

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.save()
        return instance

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('pk' ,"visit_date" )
        
    
class CreateVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = "__all__"
    def create(self, validated_data):
        visit = Visit.objects.create(**validated_data)
        return visit

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude' , instance.latitude)
        instance.longitude = validated_data.get('longitude' , instance.longitude)
        instance.visit_date = validated_data.get('visit_date' , instance.visit_date)
        instance.save()
        return instance