# Generated by Django 5.0.6 on 2024-07-07 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_remove_studentinternaltransmodel_studname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinternaltransmodel',
            old_name='papercode',
            new_name='papername',
        ),
    ]
