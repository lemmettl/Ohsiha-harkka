from django.db import models
from django.urls import reverse

class Arvostelu(models.Model):
    otsikko = models.CharField(max_length=40)
    arvosana = models.IntegerField()
    kommentti = models.CharField(max_length=100)

    def _str_ (self):                                   
        return self.otsikko

    def get_absolute_url(self):
        return reverse('update_arvostelu', kwargs={'pk': self.pk})

