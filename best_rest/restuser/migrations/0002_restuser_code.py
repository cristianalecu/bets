# Generated by Django 2.0.5 on 2018-05-21 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restuser',
            name='code',
            field=models.SmallIntegerField(default=0),
        ),
    ]
