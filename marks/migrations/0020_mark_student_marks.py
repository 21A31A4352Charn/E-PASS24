# Generated by Django 4.1.3 on 2023-02-25 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0019_remove_student_username_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('dateOfExam', models.DateField()),
                ('Marks', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='marks.mark'),
        ),
    ]
