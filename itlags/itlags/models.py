from django.db import models

class ServerGroup(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
    	return self.name

class Server(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    group = models.ForeignKey('ServerGroup', related_name='servers', on_delete=models.CASCADE)

    def __str__(self):
    	return self.name
