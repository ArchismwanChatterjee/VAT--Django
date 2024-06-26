# Generated by Django 5.0.4 on 2024-04-17 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_picfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.CharField(max_length=15)),
                ('addr', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.DeleteModel(
            name='picfile',
        ),
    ]
