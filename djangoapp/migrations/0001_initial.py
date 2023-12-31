# Generated by Django 4.2.6 on 2023-10-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='myimg')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, max_length=50)),
                ('discription', models.CharField(max_length=1000)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
