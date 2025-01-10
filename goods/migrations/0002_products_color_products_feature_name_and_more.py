# Generated by Django 5.1.3 on 2024-12-01 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='color',
            field=models.CharField(max_length=150, null=True, verbose_name='Renk'),
        ),
        migrations.AddField(
            model_name='products',
            name='feature_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Marka İsmi'),
        ),
        migrations.AddField(
            model_name='products',
            name='features_slug',
            field=models.SlugField(blank=True, max_length=200, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='products',
            name='model',
            field=models.CharField(max_length=150, null=True, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Ürün İsmi'),
        ),
    ]
