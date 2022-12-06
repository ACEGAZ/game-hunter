from django.db import models
from django.contrib.auth.models import User


class Reviews(models.Model):
    """ for customers to leave reviews """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """orders comments by date added"""
        ordering = ["-date_added"]

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"review {self.title} {self.body}"
