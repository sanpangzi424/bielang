# Generated by Django 2.0.5 on 2019-03-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userinfo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.TextField(blank=True),
        ),
    ]