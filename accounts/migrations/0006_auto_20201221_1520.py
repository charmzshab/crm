# Generated by Django 3.1.4 on 2020-12-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201221_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
