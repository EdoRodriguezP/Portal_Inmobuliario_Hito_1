from django.contrib import admin


# Register your models here.
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_filter = ["region"]  
    search_fields = ["nombre"] 

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    search_fields = ["nombre", "nro_region"]
    list_display = ["nro_region", "nombre"]


@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
  pass

@admin.register(PerfilUser)
class PerfilUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Información extra", {"fields": ("rut", "tipo_usuario","imagen")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("rut", "tipo_usuario")}),
    )