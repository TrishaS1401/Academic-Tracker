# Generated by Django 3.1.7 on 2021-05-03 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_subject_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='adsubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
