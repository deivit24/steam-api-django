# Generated by Django 4.1 on 2022-08-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steamid', models.CharField(max_length=255, unique=True)),
                ('communityvisibilitystate', models.IntegerField(null=True)),
                ('profilestate', models.IntegerField(null=True)),
                ('personaname', models.CharField(max_length=255)),
                ('profileurl', models.CharField(max_length=255)),
                ('avatar', models.CharField(max_length=255)),
                ('avatarmedium', models.CharField(max_length=255)),
                ('avatarfull', models.CharField(max_length=255)),
                ('avatarhash', models.CharField(max_length=255)),
                ('lastlogoff', models.DateTimeField(null=True)),
                ('personastate', models.IntegerField(null=True)),
                ('primaryclanid', models.CharField(max_length=255)),
                ('timecreated', models.DateTimeField(null=True)),
                ('personastateflags', models.IntegerField(null=True)),
                ('loccountrycode', models.CharField(max_length=255)),
            ],
        ),
    ]
