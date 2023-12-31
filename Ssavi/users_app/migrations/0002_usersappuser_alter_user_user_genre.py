# Generated by Django 4.2.6 on 2023-10-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersAppUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
                ('user_name', models.CharField(max_length=100)),
                ('user_genre', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'users_app_user',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='user_genre',
            field=models.CharField(max_length=200),
        ),
    ]
