# Generated by Django 4.2.6 on 2023-11-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_userpersonalinfo_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalrecipe',
            name='cooktime',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='globalrecipe',
            name='preptime',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='savedrecipe',
            name='cooktime',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='savedrecipe',
            name='preptime',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='globalrecipe',
            name='calories',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='savedrecipe',
            name='calories',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
    ]
