# Generated by Django 2.0.9 on 2019-01-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20190108_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(blank=True, to='questionnaire.Choices'),
        ),
    ]
