from django.db import models

# Create your models here.
class DjangoClasses(models.Model):
    title = models.CharField(max_length=60)
    courseNumber = models.IntegerField()
    instructor = models.CharField(max_length=60)
    duration = models.DecimalField(default=0.0, max_digits=10000, decimal_places=2)

    def __str__(self):
        return self.title
