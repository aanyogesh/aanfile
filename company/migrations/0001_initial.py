# Generated by Django 3.2.4 on 2021-06-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('phone', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('update_at', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
