from django.db import models

class DataField(models.Model):

    name = models.TextField()
    bookings = models.JSONField(null=True, blank=True)
    ph_no = models.PositiveBigIntegerField()
    time = models.TextField(blank=True, null=True)
    start = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    end = models.TextField(blank=True, null=True)
    no = models.PositiveBigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name