# Generated by Django 2.0.9 on 2019-01-08 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(null=True, to='questionnaire.Choices'),
        ),
    ]
