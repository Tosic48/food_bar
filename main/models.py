from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Cake(models.Model):
    VEGETERIAN_CHOISE = [
        ('vegeterian', 'For Vegeterian'),
        ('non_vegeterian', ' No Vegeterian'),
    ]
    title = models.CharField(max_length=100)
    layer_number = models.PositiveIntegerField()
    vegetarion_type = models.CharField(max_length=14, choices=VEGETERIAN_CHOISE)
    rating = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ])
    price = models.PositiveIntegerField
    photo = models.ImageField(upload_to='')
