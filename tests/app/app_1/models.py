from django.db import models


class RenamedConfig(models.Model):
    key_1 = models.BooleanField(null=True)
    key_2 = models.BooleanField(null=True)
