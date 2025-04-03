from django.contrib import admin
from api.models import ClientUser, TransportSchedule

@admin.register(ClientUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(TransportSchedule)
class TransportScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'transport_time', 'created_at', 'updated_at')
    list_filter = ('date',)
    search_fields = ('user__name',)