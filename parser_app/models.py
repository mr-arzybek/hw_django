from django.db import models


class FilmsKg(models.Model):
    title_name = models.CharField(max_length=100)
    title_url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title_name
