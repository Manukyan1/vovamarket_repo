# Generated by Django 2.2.2 on 2019-08-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0003_currency_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad_adding',
            name='cur_tag',
            field=models.ManyToManyField(related_name='item_cur_relname', to='marketapp.Currency_tag'),
        ),
    ]