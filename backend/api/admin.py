from django.contrib import admin
from api.models import BaseUser, ClientUser, TransportSchedule, Facility, Staff
from django.contrib.auth.admin import UserAdmin


@admin.register(BaseUser)
class StaffAdmin(UserAdmin):
    # 編集画面に表示するフィールドセット
    fieldsets = UserAdmin.fieldsets + (
        ("カスタム項目", {"fields": ("user_type",)}),
    )

    # 新規作成画面に表示するフィールドセット
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("カスタム項目", {"fields": ("user_type",)}),
    )

    # 管理画面の一覧にもカスタム項目を表示
    list_display = UserAdmin.list_display + ('user_type',)


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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = BaseUser.objects.filter(
                is_superuser=False,
                user_type="staff"
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(TransportSchedule)
class TransportScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'scheduled_transport_datetime', 'actual_transport_datetime', 'created_at', 'updated_at')
    list_filter = ('scheduled_transport_datetime',)
    search_fields = ('user__name',)