from django.core.management.base import BaseCommand
import pandas as pd
from Listing.models import Listing


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Database connections
        df = pd.read_csv('listingdata.csv')
        for address, city, postalcode, bedrooms, price, scrapedate in zip(df.address, df.city, df.postalcode, df.bedrooms, df.price, df.scrapedate):
            models = Listing(Address=address, City=city, PostalCode=postalcode,
                             Bedrooms=bedrooms, Price=price, Date=scrapedate)
            models.save()
