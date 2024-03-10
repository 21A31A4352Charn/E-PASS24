# Generated by Django 4.2 on 2023-04-30 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=5)),
                ('year', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
