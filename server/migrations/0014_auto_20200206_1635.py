# Generated by Django 3.0.2 on 2020-02-06 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_blog_detailsdesc_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='link',
            new_name='descfoot',
        ),
    ]
