# Generated by Django 3.2.3 on 2021-05-27 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_member_pw'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]
