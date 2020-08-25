# Generated by Django 2.2.6 on 2019-12-09 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191209_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_detail', to=settings.AUTH_USER_MODEL, verbose_name='Kullanici Adi'),
        ),
    ]