from django.db import models

# Create your models here.

class Comment(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.time} – {self.text}'