from django.contrib import admin

from .models import PlantRecord, ChannelData, PlantDb
# Register your models here.
admin.site.register(PlantRecord)
admin.site.register(ChannelData)
admin.site.register(PlantDb)