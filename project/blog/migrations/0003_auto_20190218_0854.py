# Generated by Django 2.1.1 on 2019-02-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190218_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]