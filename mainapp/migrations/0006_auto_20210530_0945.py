# Generated by Django 3.1.7 on 2021-05-30 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210529_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobiles',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='mobiles',
            name='img3',
        ),
        migrations.AddField(
            model_name='mobiles',
            name='cart',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='mobiles',
            name='orders',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
