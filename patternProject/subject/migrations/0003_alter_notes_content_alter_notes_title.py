# Generated by Django 4.0.3 on 2022-06-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_lecture_unique_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]