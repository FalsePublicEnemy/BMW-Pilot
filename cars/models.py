from django.db import models


class Car(models.Model):
    model = models.CharField(
        verbose_name='Model',
        max_length=64,
        db_index=True,
    )
    description = models.CharField(
        verbose_name='Description',
        max_length=300,
    )
