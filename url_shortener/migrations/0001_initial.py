# Generated by Django 2.2.7 on 2021-05-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(verbose_name='URL użytkownika')),
                ('shortened_url', models.CharField(max_length=8, unique=True, verbose_name='skrócony URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='utworzono')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='zaktualizowano')),
            ],
            options={
                'verbose_name': 'skrót adresu URL',
                'verbose_name_plural': 'skróty adresów URL',
            },
        ),
    ]
