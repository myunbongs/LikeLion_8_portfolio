from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Portfolio(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_portfolios')
    portfolio = models.ImageField(upload_to='portfolio/%Y/%m/%d', default='portfolio/no_image.png')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return '제목: %s 작성자: %s 작성일: %s' %\
               (self.title.title(), self.author.username, self.created.strftime("%Y-%m-%d %H:%M:%S"))

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', args=[str(self.id)])
