# Generated by Django 5.2 on 2025-04-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_date_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date_published",
            field=models.DateField(),
        ),
    ]
