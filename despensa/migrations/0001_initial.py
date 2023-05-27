# Generated by Django 4.2.1 on 2023-05-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantTotal', models.IntegerField()),
                ('capacidade', models.IntegerField()),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
    ]
