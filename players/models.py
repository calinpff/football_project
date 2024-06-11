from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Player(AbstractUser):
    pass


class Field(models.Model):
    name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    field_image = models.ImageField(upload_to='field_image/', default="field_image/teren_sintetic_test.png")

    def __str__(self):
        return self.name


class Match(models.Model):
    organizer = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='organizer', null=True)
    participants = models.ManyToManyField(Player, blank=True, related_name='participants')
    start_date = models.DateField(default=timezone.now)
    start_hour = models.TimeField(default=timezone.now)
    end_hour = models.TimeField(default=timezone.now)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, default=True)
    duration = models.DurationField(default=timedelta(minutes=60))
    number_of_slots = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Match will take place on {self.start_date} from {self.start_hour} to {self.end_hour}."

    def slots_available(self):
        return self.number_of_slots - self.participants.count()
