from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# model db of cakes
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


# model db reviews
class Review(models.Model):
    text: str = models.CharField(max_length=100)
    details: str = models.CharField(max_length=100)
    customers: str = models.CharField(max_length=100)
    photo: models.ImageField = models.ImageField(upload_to='')

    class Meta:
        verbose_name: str = "Отзыв"
        verbose_name_plural: str = "Отзывы"
