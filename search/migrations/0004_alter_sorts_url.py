# Generated by Django 3.2.9 on 2021-12-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_alter_sorts_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorts',
            name='url',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
