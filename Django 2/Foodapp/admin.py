from django.contrib import admin

from .models import Product, Kategorija, Klinet


# Register your models here.
class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

class KategorijaAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    list_display = ('ime', )

admin.site.register(Kategorija, KategorijaAdmin)

class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.kreator = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and request.user==obj.kreator:
            return True
        return False
admin.site.register(Product, ProductAdmin)

class KlinetAdmin(admin.ModelAdmin):
    list_display = ('ime', 'prezime')

admin.site.register(Klinet, KlinetAdmin)
