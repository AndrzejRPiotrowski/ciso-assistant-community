# Generated by Django 5.1.1 on 2024-11-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0036_asset_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="appliedcontrol",
            name="priority",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[(1, "P1"), (2, "P2"), (3, "P3"), (4, "P4")],
                null=True,
                verbose_name="Priority",
            ),
        ),
    ]