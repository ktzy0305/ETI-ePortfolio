# Generated by Django 2.2.7 on 2019-11-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]