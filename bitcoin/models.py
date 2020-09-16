from django.db import models

class Bitcoin(models.Model):
    assert_id_base = models.CharField(max_length=100, default='')
    assert_id_quote = models.CharField(max_length=100, default='')
    #rate = models.CharField(max_length=100, default='')
# Create your models here.
