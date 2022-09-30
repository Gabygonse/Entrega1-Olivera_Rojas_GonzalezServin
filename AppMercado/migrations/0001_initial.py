# Generated by Django 4.1 on 2022-09-03 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Electrodomesticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=50)),
                ('email_contacto', models.EmailField(max_length=254)),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
    ]
