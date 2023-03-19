# Generated by Django 4.1.7 on 2023-03-19 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('picture', models.FileField(upload_to='student/')),
            ],
            options={
                'db_table': 'stucents',
            },
        ),
    ]
