# Generated by Django 2.1.3 on 2018-11-17 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0005_auto_20181117_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installment',
            name='banner_linked_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='installmentnumber', to='banner.banner'),
        ),
    ]
