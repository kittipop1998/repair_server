# Generated by Django 3.1.1 on 2020-09-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0002_repair_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='up_image'),
        ),
    ]