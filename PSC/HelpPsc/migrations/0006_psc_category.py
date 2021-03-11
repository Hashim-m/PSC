# Generated by Django 3.0 on 2020-12-01 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HelpPsc', '0005_remove_psc_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='psc',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='HelpPsc.Category'),
            preserve_default=False,
        ),
    ]