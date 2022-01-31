from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    category = models.CharField(max_length=50)
    slug_category = models.SlugField(blank=True, null=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug_category = slugify(self.category)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category", kwargs={'slug': self.slug_category})

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    description = models.TextField()
    image = models.ImageField(upload_to="post_image")
    slug_post = models.SlugField(blank=True, null=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug_post = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'slug': self.slug_post})

    def __str__(self):
        return self.title
