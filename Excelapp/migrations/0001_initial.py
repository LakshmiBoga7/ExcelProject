# Generated by Django 3.1.3 on 2021-03-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myexcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BANKNAME', models.CharField(max_length=30)),
                ('IFSC', models.CharField(max_length=30)),
                ('OFFICE', models.CharField(max_length=30)),
                ('ADDRESS', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Myexcel',
            },
        ),
    ]
