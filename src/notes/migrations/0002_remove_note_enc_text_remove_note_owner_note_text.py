# Generated by Django 4.1.3 on 2022-12-05 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="enc_text",
        ),
        migrations.RemoveField(
            model_name="note",
            name="owner",
        ),
        migrations.AddField(
            model_name="note",
            name="text",
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
    ]