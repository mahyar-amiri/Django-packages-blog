# Generated by Django 4.2 on 2023-04-13 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_comment_content_main_comment_status_edited_and_more'),
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='C',
        ),
    ]
