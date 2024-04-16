from django.contrib import admin

from src.workers.models import Unit, Visit, Worker

# Register your models here.


class WorkerAdmin(admin.ModelAdmin):
    
    
    list_display = ('id', 'name')

    search_fields = ['name']
class UnitAdmin(admin.ModelAdmin):
   
    list_display = ('id', 'name' , "worker")

    search_fields = ['name']
    
    def worker(self , obj):
        return obj.worker.phone_number
    
class VisitAdmin(admin.ModelAdmin):
    def has_change_permission(self, request , obj = None):
        return False
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request,obj = None):
        return False
    list_display = ('id',"latitude" ,"longitude", "visit_date" , "unit")

    search_fields = ['unit__name' , "unit__worker__name"]
    
    def unit(self , obj):
        return obj.unit.name

admin.site.register( Worker , WorkerAdmin)
admin.site.register(Unit , UnitAdmin)
admin.site.register(Visit , VisitAdmin)
