# Generated by Django 3.2.6 on 2021-08-16 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('employees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employeemodels')),
            ],
        ),
    ]
