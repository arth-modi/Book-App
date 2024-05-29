# Generated by Django 4.2.11 on 2024-05-17 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_book2_author_alter_book2_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book2',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='website_book2_related', related_query_name='website_book2s', to='website.author'),
        ),
    ]
