# Generated by Django 3.0.2 on 2020-02-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_blog_ourteam_services_testimonial_tools'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('facebook', models.TextField()),
                ('twitter', models.TextField()),
                ('github', models.TextField()),
                ('linkedin', models.TextField()),
                ('bannerimg', models.FileField(upload_to='pics')),
                ('bodyhead', models.TextField()),
                ('quote', models.TextField()),
                ('imgright', models.FileField(upload_to='pics')),
                ('imgleft', models.FileField(upload_to='pics')),
                ('bodyfoot', models.TextField()),
            ],
        ),
    ]
