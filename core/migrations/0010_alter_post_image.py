# Generated by Django 5.0.3 on 2024-03-19 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_post_no_of_like_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]