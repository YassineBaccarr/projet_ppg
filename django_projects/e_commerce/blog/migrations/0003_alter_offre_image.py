# Generated by Django 4.2 on 2023-05-02 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_offre_image_alter_offre_type_proptiete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]