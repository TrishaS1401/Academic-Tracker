# Generated by Django 3.1.7 on 2021-05-03 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_adsubject'),
    ]

    operations = [
        migrations.AddField(
            model_name='adsubject',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
    ]
