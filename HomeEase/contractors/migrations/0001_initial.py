# Generated by Django 4.2.3 on 2023-08-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('services', models.TextField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('phone_country_code', models.IntegerField()),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
    ]
