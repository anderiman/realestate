# Generated by Django 3.0 on 2020-04-04 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hamahang', '0005_mdl_contact_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdl_apartement',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='mdl_apartement',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mdl_apartement',
            name='text',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_apartement',
            name='topic',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_contact',
            name='first_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_contact',
            name='last_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_contact',
            name='subject',
            field=models.TextField(max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_home',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='mdl_home',
            name='home',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hamahang.mdl_sale'),
        ),
        migrations.AlterField(
            model_name='mdl_home',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mdl_home',
            name='text',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_home',
            name='topic',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_land',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='mdl_land',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mdl_land',
            name='land',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hamahang.mdl_sale'),
        ),
        migrations.AlterField(
            model_name='mdl_land',
            name='text',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_land',
            name='topic',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_participation',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='mdl_participation',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mdl_participation',
            name='text',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_participation',
            name='topic',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_rent',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mdl_rent',
            name='text',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mdl_rent',
            name='topic',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
