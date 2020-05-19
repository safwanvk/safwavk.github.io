# Generated by Django 3.0.6 on 2020-05-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.EmailField(max_length=256)),
                ('subject', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=256)),
                ('image', models.FileField(max_length=256, upload_to=None)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
