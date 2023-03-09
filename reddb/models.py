from django.db import models
from django.utils import timezone


# Create your models here.
class PlantRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    plant_type = models.CharField(max_length=200)
    moisture_lvl = models.IntegerField(blank=True, null=True)
    temperature_lvl = models.IntegerField(blank=True, null=True)
    humidity_lvl = models.IntegerField(blank=True, null=True)
    light_lvl = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return str(self.name) + ': ' + str(self.id) + ': ' + str(self.time)
    
    
class ChannelData(models.Model):
    ch_id = models.BigAutoField(primary_key=True)
    ch_number = models.CharField(max_length=150)
    plant_type = models.CharField(max_length=200)
    plant_name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.ch_number) + ': ' + str(self.plant_name)
    
    
class PlantDb(models.Model):
    plant_type = models.CharField(max_length=200)
    max_moisture_lvl = models.IntegerField(default=90)
    min_moisture_lvl = models.IntegerField(default=40)
    max_temperature_lvl = models.IntegerField(blank=True, null=True)
    min_temperature_lvl = models.IntegerField(blank=True, null=True)
    max_humidity_lvl = models.IntegerField(blank=True, null=True)
    min_humidity_lvl = models.IntegerField(blank=True, null=True)
    min_light_lvl = models.IntegerField(blank=True, null=True)
    max_light_lvl = models.IntegerField(blank=True, null=True)
    
    daylight_time = models.IntegerField(blank=True, null=True) # in hours per day
    amount_water = models.IntegerField(blank=True, null=True)
    hours_between_watering = models.IntegerField(blank=True, null=True) #in hours
    
    
    def __str__(self):
        return str(self.plant_type)