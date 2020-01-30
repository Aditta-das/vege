from django.db import models
from django.contrib.auth.models import User, auth

class Detail(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    is_stock = models.BooleanField(blank=False)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    massage = models.TextField('massage')
    date_comment = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return '{} by {}'.format(self.user_id, self.post_id)
