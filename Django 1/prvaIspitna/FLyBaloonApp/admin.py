from django.contrib import admin
from .models import Pilot
from .models import Ballon
from .models import Let
from .models import AviokompanijaPilot
from .models import Aviokompanija

# Register your models here.


class PilotAdmin(admin.ModelAdmin):
    list_display = ('ime', 'prezime', )


admin.site.register(Pilot, PilotAdmin)


class BallonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ballon, BallonAdmin)


class LetAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.kreator = request.user
        super().save_model(request,obj,form,change)

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.kreator:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Let, LetAdmin)


class AviokompanijaPilotAdmin(admin.StackedInline):
    model = AviokompanijaPilot


class AviokompanijaAdmin(admin.ModelAdmin):
    inlines = [AviokompanijaPilotAdmin, ]


admin.site.register(Aviokompanija, AviokompanijaAdmin)