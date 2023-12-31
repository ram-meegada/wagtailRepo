# Generated by Django 4.2.3 on 2023-07-21 11:15

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', max_length=255)), ('text', wagtail.blocks.TextBlock(help_text='Add additional text', max_length=255))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
