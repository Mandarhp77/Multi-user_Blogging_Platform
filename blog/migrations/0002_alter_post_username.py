# Generated by Django 4.2 on 2023-08-29 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post", name="username", field=models.CharField(max_length=20),
        ),
    ]