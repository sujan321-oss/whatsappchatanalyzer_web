# Generated by Django 4.2.5 on 2023-09-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhatsAppFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueidentifier', models.CharField(max_length=100)),
                ('file', models.FileField(default=False, upload_to='chatfile')),
            ],
        ),
    ]
