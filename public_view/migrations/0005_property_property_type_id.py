# Generated by Django 3.1.1 on 2021-03-26 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public_view', '0004_auto_20210326_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property_type', to='public_view.propertytype'),
            preserve_default=False,
        ),
    ]
