# Generated by Django 4.0.3 on 2022-03-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tider', '0004_post_hashtags'),
    ]

    operations = [
        migrations.AddField(
            model_name='subreddit',
            name='posts',
            field=models.ManyToManyField(blank=True, null=True, to='tider.post'),
        ),
    ]
