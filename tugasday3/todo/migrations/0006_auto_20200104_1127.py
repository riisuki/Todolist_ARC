# Generated by Django 3.0.2 on 2020-01-04 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todo_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
