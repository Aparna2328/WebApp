# Generated by Django 5.0.7 on 2024-07-26 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=255)),
                ('Address1', models.CharField(max_length=255)),
                ('Address2', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=255)),
                ('Phn_no', models.IntegerField()),
                ('City', models.CharField(max_length=100)),
                ('Zip', models.IntegerField()),
            ],
        ),
    ]