# Generated by Django 5.0.6 on 2024-06-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_alter_field_field_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_image',
            field=models.ImageField(default='media/field_image/teren_sintetic_test.png', upload_to='field_image/'),
        ),
    ]
