# Generated by Django 3.2.4 on 2021-07-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_messagereport_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagereport',
            name='content',
            field=models.CharField(default='Paste Content Here', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='messagereport',
            name='username',
            field=models.CharField(default='Reported Person', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userreport',
            name='username',
            field=models.CharField(default='Reported Person', max_length=200, null=True),
        ),
    ]