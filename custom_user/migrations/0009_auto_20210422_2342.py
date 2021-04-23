# Generated by Django 3.1.5 on 2021-04-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countdown_core', '0007_reactionset'),
        ('custom_user', '0008_auto_20210421_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bookmarked_countdowns',
            field=models.ManyToManyField(related_name='user_bookmarks', to='countdown_core.Countdown'),
        ),
    ]
