from django.db import models

class Sector(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name
