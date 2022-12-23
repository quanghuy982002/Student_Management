# Generated by Django 2.2 on 2022-12-20 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0004_remove_students_major_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='major_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.Major'),
        ),
    ]
