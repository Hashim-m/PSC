# Generated by Django 3.0 on 2020-12-01 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HelpPsc', '0006_psc_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.RemoveField(
            model_name='psc',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Psc',
        ),
    ]
