# Generated by Django 2.2 on 2022-12-20 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='major',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('major_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.Courses')),
            ],
        ),
    ]