# Generated by Django 2.1.5 on 2020-06-01 09:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0006_auto_20200601_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landscape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('text_content', models.TextField(default=None)),
                ('main_color', models.CharField(choices=[('B', 'Blue'), ('G', 'Green'), ('R', 'Red'), ('Y', 'Yellow'), ('BR', 'Brown'), ('W', 'White'), ('BL', 'Black'), ('O', 'Other')], default='Blue', max_length=30)),
                ('landscape_type', models.CharField(choices=[('forest', 'Forest'), ('dessert', 'Dessert'), ('city', 'City'), ('mountains', 'Mountains')], default='Blue', max_length=30)),
                ('image', models.ImageField(default='default.jpg', upload_to='graphic_image')),
                ('date_made', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graphics.Category')),
            ],
        ),
    ]
