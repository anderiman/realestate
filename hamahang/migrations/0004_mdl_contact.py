# Generated by Django 3.0 on 2020-04-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamahang', '0003_auto_20200401_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='mdl_Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('subject', models.TextField(max_length=4000)),
            ],
        ),
    ]
