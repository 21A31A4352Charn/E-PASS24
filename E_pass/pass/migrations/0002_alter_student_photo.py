# Generated by Django 4.2 on 2023-04-30 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.FileField(upload_to='images/'),
        ),
    ]