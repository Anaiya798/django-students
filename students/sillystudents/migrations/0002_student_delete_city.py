# Generated by Django 4.0 on 2021-12-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sillystudents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('patronic', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]