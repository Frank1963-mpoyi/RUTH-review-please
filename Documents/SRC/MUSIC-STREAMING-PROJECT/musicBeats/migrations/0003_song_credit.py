# Generated by Django 3.0.8 on 2021-03-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicBeats', '0002_auto_20210324_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='credit',
            field=models.CharField(default='', max_length=100000),
        ),
    ]