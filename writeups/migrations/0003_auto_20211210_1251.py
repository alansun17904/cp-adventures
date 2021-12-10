# Generated by Django 3.2.10 on 2021-12-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0002_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='writeups.Tag'),
        ),
    ]