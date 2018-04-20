# Generated by Django 2.0.3 on 2018-04-20 01:53

from django.db import migrations, models
import django.db.models.deletion
import sharp.utls


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20180420_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.CharField(max_length=250)),
                ('ar_name', models.CharField(max_length=250)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=sharp.utls.upload_location)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='services.Service')),
            ],
        ),
    ]
