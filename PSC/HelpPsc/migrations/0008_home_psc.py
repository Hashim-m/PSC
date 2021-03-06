# Generated by Django 3.0 on 2020-12-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('HelpPsc', '0007_auto_20201201_1751'),
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
        migrations.CreateModel(
            name='Psc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400)),
                ('apple', models.CharField(max_length=100)),
                ('boy', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=100)),
                ('dog', models.CharField(max_length=100)),
                ('answer', models.TextField(max_length=400)),
            ],
        ),
    ]
