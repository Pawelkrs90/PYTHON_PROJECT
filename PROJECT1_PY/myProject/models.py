from django.db import models
from django.utils import timezone

class Customer(models.Model):

    CustomerId = models.ForeignKey
    Wzrost = models.CharField(max_length=200)
    Imie = models.TextField()
    Nazwisko = models.TextField()
    BirthDate = models.DateTimeField(default=timezone.now)

    def zapiszCustomera(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Imie

