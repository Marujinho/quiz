# Generated by Django 3.2.7 on 2021-09-02 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30)),
                ('info', models.CharField(max_length=90)),
                ('economics', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
