# Generated by Django 3.1.1 on 2021-11-23 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sorts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('spell_resistance', models.BooleanField(default=False)),
                ('is_verbal', models.BooleanField(default=False)),
                ('is_somatic', models.BooleanField(default=False)),
                ('is_material', models.BooleanField(default=False)),
                ('max_level', models.IntegerField(default=0)),
                ('classes', models.ManyToManyField(to='search.Classes')),
                ('monsters', models.ManyToManyField(to='search.Monster')),
            ],
        ),
    ]
