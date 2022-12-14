# Generated by Django 4.1.1 on 2022-09-20 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="admindetails",
            fields=[
                ("user_id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "username",
                    models.CharField(
                        blank=True, default=None, max_length=60, null=True
                    ),
                ),
                ("signup_otp", models.CharField(max_length=4)),
                ("emailId", models.EmailField(max_length=254)),
                (
                    "password",
                    models.CharField(
                        error_messages={"required": "Password cannot be null"},
                        max_length=8,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Books",
            fields=[
                ("book_id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(
                        blank=True, default=None, max_length=60, null=True
                    ),
                ),
                (
                    "title1",
                    models.CharField(
                        blank=True, default=None, max_length=60, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="issued_books",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "issued_to",
                    models.CharField(
                        blank=True, default=None, max_length=60, null=True
                    ),
                ),
                (
                    "book_id",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="books.books",
                    ),
                ),
            ],
        ),
    ]
