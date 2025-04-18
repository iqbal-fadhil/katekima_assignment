# Generated by Django 5.2 on 2025-04-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_purchasedetail_created_at_purchasedetail_is_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='selldetail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='selldetail',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='selldetail',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='sellheader',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='sellheader',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
