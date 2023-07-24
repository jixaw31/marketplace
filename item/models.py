from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE, )

    class Meta:
        verbose_name_plural = 'items'

    def __str__(self):
        return self.name


class ConversationMessage(models.Model):
    text = models.TextField(max_length=250)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-sent_at',)

    def __str__(self):
        return self.text[:30]
