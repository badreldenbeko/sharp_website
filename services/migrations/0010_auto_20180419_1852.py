# Generated by Django 2.0.3 on 2018-04-19 16:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20180408_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='ar_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='en_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]