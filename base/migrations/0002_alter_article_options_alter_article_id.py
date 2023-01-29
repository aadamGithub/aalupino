# Generated by Django 4.1.2 on 2023-01-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created'], 'permissions': (('can_create_article', 'Create new article'), ('can_update_article', 'Update an article'), ('can_delete_article', 'Delete an article'))},
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.CharField(editable=False, max_length=200, primary_key=True, serialize=False),
        ),
    ]