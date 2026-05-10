from django.db import models


class TravelUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    destination = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name