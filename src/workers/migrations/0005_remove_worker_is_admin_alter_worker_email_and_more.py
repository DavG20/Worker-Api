# Generated by Django 5.0.3 on 2024-03-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workers", "0004_alter_worker_managers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="worker",
            name="is_admin",
        ),
        migrations.AlterField(
            model_name="worker",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="worker",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
        migrations.AlterField(
            model_name="worker",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
    ]
