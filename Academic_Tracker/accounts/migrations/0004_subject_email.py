# Generated by Django 3.1.7 on 2021-05-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_adminr_studentsr'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
    ]
