# Generated by Django 4.2.4 on 2023-08-15 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_work_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='months',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='経験月数'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='years',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='経験年数'),
        ),
    ]