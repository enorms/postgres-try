# Generated by Django 4.0.3 on 2022-03-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgrestry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greeting',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='greeting',
            name='hackernews_username',
        ),
        migrations.AddField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, default=1, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='greeting',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]