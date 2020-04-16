# Generated by Django 3.0.5 on 2020-04-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='experience',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='firstname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]