# Generated by Django 3.0b1 on 2019-11-13 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copro_profiles', '0002_auto_20191113_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamlink',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_links', to='copro_profiles.Team'),
        ),
    ]
