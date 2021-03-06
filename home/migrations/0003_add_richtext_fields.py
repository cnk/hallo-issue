# Generated by Django 3.2 on 2021-04-26 20:12

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image_panels',
            field=wagtail.core.fields.StreamField([('ImagePanel', wagtail.core.blocks.StreamBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.RichTextBlock())]))], blank=True, null=True),
        ),
    ]
