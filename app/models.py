
from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('active', 'Faol'),
        ('inactive', 'Nofaol'),
    ]

    title = models.CharField("Kitob nomi", max_length=100)
    author = models.CharField("Muallif", max_length=100)
    status = models.CharField("Holat", max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

