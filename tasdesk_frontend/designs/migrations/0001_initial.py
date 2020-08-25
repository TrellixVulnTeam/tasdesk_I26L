# Generated by Django 2.2.6 on 2019-12-09 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_title', models.CharField(max_length=120, verbose_name='Tasarım Başlığı')),
                ('design_content', models.TextField(verbose_name='Tasarım İçeriği')),
                ('publishing_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Tarihi')),
                ('design_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('is_public', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=False, to='home.Categories', verbose_name='Kategori')),
                ('likes', models.ManyToManyField(blank=True, related_name='design_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'ordering': ['-publishing_date', 'id'],
            },
        ),
        migrations.CreateModel(
            name='DesignView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40)),
                ('session', models.CharField(max_length=40)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='designs.Design', verbose_name='Tasarım')),
            ],
        ),
        migrations.CreateModel(
            name='DesignComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField(verbose_name='Yorum')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='designs.Design', verbose_name='Tasarım')),
                ('user', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
