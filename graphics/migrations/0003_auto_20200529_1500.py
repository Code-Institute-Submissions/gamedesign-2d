# Generated by Django 2.1.5 on 2020-05-29 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0002_auto_20200529_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designtype',
            name='text_content',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='designtype',
            name='title',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
