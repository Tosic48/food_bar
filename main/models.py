from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cakes(models.Model):
    VEGETERIAN_CHOISE = [
        ('vegeterian', 'For Vegeterian'),
        ('non_vegeterian', ' No Vegeterian'),
    ]
    title = models.CharField(max_length=100)
    composition = models.CharField(max_length=100)
    layer_number = models.PositiveIntegerField()
    vegetarion_type = models.CharField(max_length=14, choices=VEGETERIAN_CHOISE)
    rating = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ])
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Торт"
        verbose_name_plural = "Торты"


class Review(models.Model):
    text = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    customers = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='')

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
