# Generated by Django 3.0 on 2020-11-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpPsc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
