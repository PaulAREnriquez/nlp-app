# Generated by Django 4.1.5 on 2023-01-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentimentmodel',
            name='review',
            field=models.CharField(max_length=1000),
        ),
    ]
