# Generated by Django 4.1.2 on 2023-01-26 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_article_timetaken'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created']},
        ),
    ]
