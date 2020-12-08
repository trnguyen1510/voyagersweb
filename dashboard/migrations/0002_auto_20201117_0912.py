# Generated by Django 3.0.5 on 2020-11-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address1',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fb_handle',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='insta_handle',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telephone',
            field=models.CharField(blank=True, default='', max_length=13),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_handle',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, default=''),
        ),
    ]
