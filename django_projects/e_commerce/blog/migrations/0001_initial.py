# Generated by Django 4.1.7 on 2023-04-29 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop_id', models.IntegerField(blank=True, null=True)),
                ('type_proptiete', models.CharField(blank=True, max_length=20)),
                ('surface', models.CharField(default='', max_length=50)),
                ('nbr_chambre', models.PositiveIntegerField(default=0)),
                ('nbr_sallebain', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('type', models.CharField(default='', max_length=20)),
                ('address', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('existe', models.BooleanField(default=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modif', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Prix en dinar', max_digits=10)),
            ],
            options={
                'db_table': '1',
            },
        ),
        migrations.CreateModel(
            name='Vendeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=20)),
                ('address', models.CharField(blank=True, default='', max_length=20, null=True)),
            ],
            options={
                'db_table': 'vendeur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Besoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_max', models.PositiveBigIntegerField()),
                ('type_propiete', models.CharField(max_length=20)),
                ('surface_min', models.CharField(max_length=50)),
                ('localisation', models.CharField(max_length=50)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('offre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.offre')),
            ],
            options={
                'db_table': 'besoin',
            },
        ),
    ]