from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as gl


class Traveler(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='traveler',
        null=True,
        blank=True
    )
    nickname = models.CharField(
        max_length=30,
        unique=True,
        help_text="*Nicknames can contain only letters and digits."
    )
    email = models.EmailField(
        max_length=30,
        unique=True
    )
    country = models.CharField(
        max_length=3
    )
    about_me = models.TextField(
        blank=True,
        null=True
    )

    def clean(self):
        if not self.nickname.isalnum() or len(self.nickname) < 3:
            raise ValidationError(gl("Your nickname is invalid!"))
        if len(self.country) != 3:
            raise ValidationError(gl("Country must be exactly 3 characters."))

    def ordered_trips(self):
        return self.trips.all().order_by('-start_date')  # Order trips by start_date descending

    def __str__(self):
        return self.nickname


class Trip(models.Model):
    destination = models.CharField(
        max_length=100
    )
    summary = models.TextField()
    start_date = models.DateField()
    duration = models.PositiveSmallIntegerField(
        default=1,
        help_text="*Duration in days is expected."
    )
    image_url = models.URLField(
        blank=True,
        null=True
    )
    traveler = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE,
        related_name="trips"
    )

    def clean(self):
        if len(self.destination) < 3 or len(self.destination) > 100:
            raise ValidationError(gl("Destination must be between 3 and 100 characters."))

    def __str__(self):
        return self.destination
