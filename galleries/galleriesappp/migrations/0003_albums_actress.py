# Generated by Django 3.1.1 on 2020-09-15 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleriesappp', '0002_actress_bannerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='actress',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='galleriesappp.actress'),
        ),
    ]
