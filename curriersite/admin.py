from django.contrib import admin

from .models import Visitor


# Register your models here.
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'ip_address', 'city', 'name', 'visit_date')
    readonly_fields = ('visit_date',)