# Generated by Django 4.1.1 on 2022-10-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='xyz.jpg', upload_to='media'),
        ),
    ]
