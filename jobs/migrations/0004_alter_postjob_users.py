# Generated by Django 4.0.3 on 2022-05-12 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_applyvacancy_date_applyvacancy_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postjob',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.usereegistration'),
        ),
    ]
