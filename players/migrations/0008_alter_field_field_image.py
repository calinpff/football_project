# Generated by Django 5.0.6 on 2024-06-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_alter_match_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_image',
            field=models.ImageField(blank=True, null=True, upload_to='field_image/'),
        ),
    ]
