# Generated by Django 3.0.5 on 2020-04-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=models.TextField(),
        ),
    ]
