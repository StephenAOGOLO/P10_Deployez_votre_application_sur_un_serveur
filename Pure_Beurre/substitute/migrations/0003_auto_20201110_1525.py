# Generated by Django 3.1.2 on 2020-11-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substitute', '0002_auto_20201109_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='id_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
