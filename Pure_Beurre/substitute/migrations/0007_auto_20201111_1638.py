# Generated by Django 3.1.2 on 2020-11-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substitute', '0006_auto_20201111_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='fk_name',
        ),
        migrations.AlterField(
            model_name='aliment',
            name='tag',
            field=models.ManyToManyField(to='substitute.Category'),
        ),
    ]
