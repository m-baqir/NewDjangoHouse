from django.db import models

# Create your models here.
class Listing(models.Model):
    Address = models.CharField('Address', max_length=250)
    Price = models.CharField('Price', max_length=250)
    Bedrooms = models.IntegerField('Bedrooms')
    City = models.CharField('City', max_length=250)
    Date = models.DateTimeField('Date Scraped')
    PostalCode = models.CharField('Postal Code', max_length=20)

    def __str__(self):
        return self.Address
