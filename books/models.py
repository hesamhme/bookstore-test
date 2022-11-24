from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Books(models.Model):
    STATUS_CHOICE = (
        ('fa', 'farsi'),
        ('en', 'english'),
        ('etc', 'other')
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    language = models.CharField(max_length=50, choices=STATUS_CHOICE)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return f"{self.title}  : {self.author}  : {self.price}"

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    creat_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book} : {self.user}  : {self.creat_at}"





