# Generated by Django 4.2 on 2023-04-30 17:47

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("content", models.CharField(blank=True, max_length=4096, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("data", models.JSONField(null=True)),
                ("session_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("page_number", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
