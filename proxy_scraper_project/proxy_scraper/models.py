from django.db import models

class Proxy(models.Model):
    ip = models.CharField(max_length=100)
    port = models.IntegerField()
    protocol = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    uptime = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ip}:{self.port}"
