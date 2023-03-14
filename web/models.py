from django.db import models

# Create your models here.
class ClientStats(models.Model):
    client_name = models.CharField(max_length=120)
    auto_mode = models.BooleanField(default=False)
    stats = models.CharField(max_length=2000)
    status = models.CharField(max_length=2000)
    
    def __str_(self):
        return self.client_name
    
    
