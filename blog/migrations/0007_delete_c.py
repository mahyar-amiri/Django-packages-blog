# Generated by Django 4.2 on 2023-04-13 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_comment_c'),
    ]

    operations = [
        migrations.DeleteModel(
            name='C',
        ),
    ]