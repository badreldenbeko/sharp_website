# Generated by Django 2.0.3 on 2018-04-20 18:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import sharp.utls


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.CharField(max_length=200)),
                ('ar_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('en_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('ar_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=sharp.utls.upload_location)),
                ('publish_on_home', models.BooleanField(default=False)),
                ('publish_pricing', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_client_name', models.CharField(max_length=250)),
                ('ar_client_name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=sharp.utls.upload_location)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='services.Service')),
            ],
        ),
        migrations.CreateModel(
            name='ServicePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_title', models.CharField(max_length=200)),
                ('ar_title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('en_body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('ar_body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=sharp.utls.upload_location)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='services.Service')),
            ],
        ),
        migrations.CreateModel(
            name='ServicePostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('service_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='services.ServicePost')),
            ],
        ),
        migrations.CreateModel(
            name='ServicePostVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('video', models.CharField(blank=True, max_length=250, null=True)),
                ('en_video_name', models.CharField(max_length=250)),
                ('ar_video_name', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='services.ServicePost')),
            ],
        ),
        migrations.CreateModel(
            name='ServicePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_price_title', models.CharField(max_length=200)),
                ('ar_price_title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('en_detail', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('ar_detail', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='services.Service')),
            ],
        ),
    ]
