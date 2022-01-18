from django.db import models

class DataField(models.Model):

    name = models.TextField()
    ph_no = models.PositiveBigIntegerField()
    time = models.TextField()
    start = models.TextField()
    end = models.TextField()

    def __str__(self):
        return self.name