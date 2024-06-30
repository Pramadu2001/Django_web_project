# Generated by Django 5.0.6 on 2024-06-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('description', models.TextField()),
                ('material', models.TextField(default='')),
                ('category', models.CharField(choices=[('FW', 'FormalWear'), ('Mw', 'MensWear'), ('AC', 'Accessories'), ('KW', 'KidsWear'), ('CW', 'CasualWear'), ('WW', 'WomensWear')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
