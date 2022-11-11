from django.db import models


class Books(models.Model):
    STATUS_CHOICE = (
        ('fa', 'farsi'),
        ('en', 'english'),
        ('etc', 'other')
    )
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    language = models.CharField(max_length=50, choices=STATUS_CHOICE)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

