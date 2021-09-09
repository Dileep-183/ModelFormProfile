# Generated by Django 2.2 on 2021-09-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=10)),
                ('urls', models.URLField()),
                ('about_me', models.TextField()),
                ('password', models.CharField(max_length=20)),
                ('is_staff', models.BooleanField(default=0)),
                ('date_of_joining', models.DateField()),
            ],
            options={
                'db_table': 'Profile',
            },
        ),
    ]
