from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(ServicesOfOrder)
class ServicesOfOrderAdmin(admin.ModelAdmin):
    pass

@admin.register(PartsOfOrder)
class PartsOfOrderAdmin(admin.ModelAdmin):
    pass

