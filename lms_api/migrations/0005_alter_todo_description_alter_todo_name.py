# Generated by Django 4.2.16 on 2024-11-28 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_api', '0004_todo_remove_assignment_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]