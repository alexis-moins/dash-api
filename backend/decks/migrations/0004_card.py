# Generated by Django 4.1 on 2022-08-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0003_delete_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.CharField(max_length=300)),
                ('back', models.CharField(max_length=300)),
            ],
        ),
    ]