# Generated by Django 2.1.5 on 2020-06-13 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designs',
            name='category',
        ),
        migrations.AddField(
            model_name='designs',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='graphics.Category'),
        ),
    ]
