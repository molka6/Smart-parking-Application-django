# Generated by Django 3.1.4 on 2021-02-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app0', '0002_user_cin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=50312458, max_length=15),
            preserve_default=False,
        ),
    ]
