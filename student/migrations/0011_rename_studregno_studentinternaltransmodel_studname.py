# Generated by Django 5.0.6 on 2024-07-12 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_alter_batchmastermodel_batchid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinternaltransmodel',
            old_name='studregno',
            new_name='studname',
        ),
    ]
