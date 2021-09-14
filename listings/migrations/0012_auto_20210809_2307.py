# Generated by Django 3.2.5 on 2021-08-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20210807_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='is_let',
        ),
        migrations.RemoveField(
            model_name='listings',
            name='is_sale',
        ),
        migrations.AddField(
            model_name='listings',
            name='condition',
            field=models.CharField(choices=[('let', 'اجاره'), ('sale', 'فروش')], default='اجااره', max_length=128),
        ),
    ]