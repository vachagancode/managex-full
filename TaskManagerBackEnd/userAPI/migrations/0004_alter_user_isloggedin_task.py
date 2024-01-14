# Generated by Django 5.0 on 2024-01-12 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAPI', '0003_alter_user_isloggedin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isLoggedIn',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=166)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAPI.user')),
            ],
        ),
    ]