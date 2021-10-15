from django.db import models
from django.urls import reverse

# Create your models here.

class CategoryFarmProduce(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category farm produce'
        verbose_name_plural = 'categories farm produce'

    def get_url(self):
            return reverse('Category_farm_produce_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name