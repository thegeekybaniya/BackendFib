# Generated by Django 3.0.3 on 2020-02-23 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0002_auto_20200223_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organisation.Project'),
        ),
    ]
