# Generated by Django 3.1.1 on 2020-09-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleriesappp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actress',
            name='bannerImage',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]