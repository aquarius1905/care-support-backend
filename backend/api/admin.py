from django.contrib import admin
from api.models import ClientUser, TransportSchedule, Facility, Staff


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(TransportSchedule)
class TransportScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'scheduled_transport_datetime', 'actual_transport_datetime', 'created_at', 'updated_at')
    list_filter = ('scheduled_transport_datetime',)
    search_fields = ('user__name',)