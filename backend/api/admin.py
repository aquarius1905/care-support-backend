from django.contrib import admin
from transport.models import User, TransportSchedule

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(TransportSchedule)
class TransportScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'transport_time', 'created_at', 'updated_at')
    list_filter = ('date',)
    search_fields = ('user__name',)