# Generated by Django 5.0 on 2024-01-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAPI', '0004_alter_user_isloggedin_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
