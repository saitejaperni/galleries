# Generated by Django 3.1.1 on 2020-09-21 03:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleriesappp', '0003_albums_actress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]