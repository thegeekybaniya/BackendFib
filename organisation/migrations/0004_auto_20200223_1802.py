# Generated by Django 3.0.3 on 2020-02-23 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0003_auto_20200223_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Admin'),
        ),
    ]
