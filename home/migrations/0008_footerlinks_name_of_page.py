# Generated by Django 4.2.3 on 2023-07-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_footerlinks_id_alter_homeimages_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='footerlinks',
            name='name_of_page',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]