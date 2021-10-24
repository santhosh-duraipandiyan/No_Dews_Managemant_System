# Generated by Django 3.2.8 on 2021-10-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_verefication_requests_verification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='Verification',
            new_name='Hostel',
        ),
        migrations.AddField(
            model_name='requests',
            name='Labs',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='Library',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='NSS',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='Office',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='PE',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='Dept',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
