# Generated by Django 2.2.7 on 2019-11-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0034_service_account_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reg_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
