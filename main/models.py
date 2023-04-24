from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


def validate_image(image):
    if image.height != 270 or image.width != 370:
        raise ValidationError(_('Invalid dimensions, image dimensions must be 370x270px'))


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(validators=[validate_image])
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    
class Unit(models.Model):
    term = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.term


def greater_than_zero(value):
    if value <= 0:
        raise ValidationError(_('Invalid price'))

def distinct_one_hundred_percent(value):
    if value == 100:
        raise ValidationError(_('Invalid discount'))


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(validators=[validate_image])
    description = models.CharField(max_length=180)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name='products', on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.FloatField(validators=[greater_than_zero])
    discount = models.PositiveSmallIntegerField(default=0, validators=[distinct_one_hundred_percent])
    max_unit = models.PositiveSmallIntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' X ' + str(self.quantity) + ' ' + str(self.unit)

    # todo: override and slugify