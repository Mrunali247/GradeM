# Generated by Django 4.1.5 on 2023-03-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='classTeacher',
            field=models.BooleanField(default=1),
        ),
    ]
