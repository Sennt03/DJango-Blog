# Generated by Django 3.2 on 2021-05-11 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='img',
            new_name='image',
        ),
    ]