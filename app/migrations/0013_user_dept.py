# Generated by Django 3.2.8 on 2021-11-29 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_student_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Dept',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
