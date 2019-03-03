from django.db import models


class Config(models.Model):
    key_1 = models.BooleanField(null=True)
    key_2 = models.BooleanField(null=True)
