# Generated by Django 2.2.6 on 2019-12-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=100, verbose_name='Kategori Başlığı')),
                ('category_content', models.TextField(null=True, verbose_name='Kategori Açıklaması')),
                ('publishing_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Tarihi')),
            ],
        ),
    ]
