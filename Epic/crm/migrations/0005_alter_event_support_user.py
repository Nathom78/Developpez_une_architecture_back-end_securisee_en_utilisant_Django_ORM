# Generated by Django 4.2.3 on 2023-07-15 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0004_alter_client_email_alter_client_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='support_user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='support contact'),
        ),
    ]
