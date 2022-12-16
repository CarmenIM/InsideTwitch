from django.db import models


class BlogPost(models.Model):
    nume = models.CharField(max_length=120)
    pisica = models.CharField(max_length=120)
    atributii = models.CharField(max_length=120)

    def __str__(self):
        return self.nume
