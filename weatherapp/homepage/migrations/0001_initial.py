# Generated by Django 4.1 on 2022-08-10 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
                ('state_name', models.CharField(blank=True, max_length=200, null=True)),
                ('country_name', models.CharField(max_length=200)),
            ],
        ),
    ]