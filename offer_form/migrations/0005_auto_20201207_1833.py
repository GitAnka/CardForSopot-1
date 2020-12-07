# Generated by Django 3.1.3 on 2020-12-07 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer_form', '0004_offers_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='offers',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='offer_form.category'),
        ),
    ]
