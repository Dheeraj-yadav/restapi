from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    salary = models.IntegerField()

    def __str__(self):
        return self.name

