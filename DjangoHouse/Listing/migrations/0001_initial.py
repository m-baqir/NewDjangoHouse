# Generated by Django 3.2.8 on 2021-10-20 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=250, verbose_name='Address')),
                ('Price', models.CharField(max_length=250, verbose_name='Price')),
                ('Bedrooms', models.IntegerField(verbose_name='Bedrooms')),
                ('City', models.CharField(max_length=250, verbose_name='City')),
                ('Date', models.DateTimeField(verbose_name='Date Scraped')),
                ('PostalCode', models.CharField(max_length=20, verbose_name='Postal Code')),
            ],
        ),
    ]
