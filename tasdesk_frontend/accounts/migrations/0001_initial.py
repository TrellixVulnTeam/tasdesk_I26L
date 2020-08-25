# Generated by Django 2.2.6 on 2019-12-09 12:28

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_designer', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='User_Reviews',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(verbose_name='Gorus')),
                ('user_id', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Kullanici Adi')),
            ],
        ),
        migrations.CreateModel(
            name='User_Messages',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('message_title', models.CharField(max_length=100, verbose_name='Mesaj Basligi')),
                ('message_content', models.TextField(verbose_name='Mesaj Icerigi')),
                ('user_id', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Kullanici Adi')),
            ],
        ),
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduations', models.TextField(verbose_name='Egitim Bilgileri')),
                ('experiences', models.TextField(verbose_name='Deneyimler')),
                ('skills', models.TextField(verbose_name='Yetenekler')),
                ('location', models.TextField(verbose_name='Lokasyon')),
                ('about', models.TextField(verbose_name='Hakkinda')),
                ('user_profile_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Profil Fotografi')),
                ('user_job', models.CharField(max_length=75, verbose_name='Meslek')),
                ('followers', models.IntegerField(default=0)),
                ('followed', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Kullanici Adi')),
            ],
        ),
    ]