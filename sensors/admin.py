from django.contrib.admin import site, ModelAdmin
from .models import Sensors, Measurements


# Register your models here.
site.register(Sensors, ModelAdmin)
site.register(Measurements, ModelAdmin)
