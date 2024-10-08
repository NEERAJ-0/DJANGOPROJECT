# Generated by Django 5.0.6 on 2024-07-07 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_rename_batchmaster_batchmastermodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinternaltransmodel',
            name='studname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_name_trans', to='student.studentmastermodel'),
        ),
        migrations.AlterField(
            model_name='studentinternaltransmodel',
            name='studregno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_reg_trans', to='student.studentmastermodel'),
        ),
    ]
