from django.db import models

# Create your models here.

TYPE_CHOICES = {
    ('appetizers', 'appetizers'),
    ('entrees', 'entrees'),
    ('treats', 'treats'),
    ('drinks', 'drinks'),
}
# we create this dictionary that will now be fed into our type field of Product class

class Product(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    # adding choices says there will be a choice(drop down box) and we give it the value of TYPE_CHOICES
    # so it references the dictionary we just made
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
        # invoking string and returns object description as string of self.name (test)
