# Generated by Django 3.1.2 on 2020-12-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substitute', '0017_auto_20201123_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=2, null=True)),
                ('mentions_title', models.CharField(max_length=1000, null=True)),
                ('mentions_id_fn', models.CharField(max_length=1000, null=True)),
                ('mentions_id_ln', models.CharField(max_length=1000, null=True)),
                ('mentions_id_ph', models.CharField(max_length=1000, null=True)),
                ('mentions_id_m', models.CharField(max_length=1000, null=True)),
                ('mentions_id_pn', models.CharField(max_length=1000, null=True)),
                ('mentions_id_s', models.CharField(max_length=1000, null=True)),
                ('mentions_a_rcs', models.CharField(max_length=1000, null=True)),
                ('mentions_a_fn', models.CharField(max_length=1000, null=True)),
                ('mentions_a_cgv', models.CharField(max_length=1000, null=True)),
                ('mentions_cookies', models.CharField(max_length=1000, null=True)),
                ('home_s', models.CharField(max_length=1000, null=True)),
                ('home_c', models.CharField(max_length=1000, null=True)),
                ('home_bm', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
