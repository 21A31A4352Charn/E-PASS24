# Generated by Django 4.1.3 on 2023-02-25 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0016_alter_student_managers_alter_student_marks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='marks',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.DeleteModel(
            name='mark',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]