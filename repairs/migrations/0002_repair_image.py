# Generated by Django 3.1.1 on 2020-09-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='image',
            field=models.FileField(blank=True, upload_to='up_image'),
        ),
    ]
