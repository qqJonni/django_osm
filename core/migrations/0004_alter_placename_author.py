# Generated by Django 4.2.7 on 2023-12-04 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0003_alter_placename_published_at_alter_placename_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="placename",
            name="author",
            field=models.ForeignKey(
                default="admin",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
    ]