from django.contrib import admin
from .models import Event, Band, BandEvent


# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ('ime', 'imeDrzava')
admin.site.register(Band, BandAdmin)

class BandEventAdmin(admin.StackedInline):
    model = BandEvent
class EventAdmin(admin.ModelAdmin):
    inlines = [BandEventAdmin, ]
    list_display = ('ime', 'vremeOdrzuvanje')
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            obj.kreator = request.user
            super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and request.user==obj.kreator:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user==obj.kreator:
            return True
        return False

admin.site.register(Event, EventAdmin)

#Настаните се прикажуваат со име и датум, а бендовите со име и држава на потекло