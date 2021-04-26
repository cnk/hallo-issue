from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock

class ImagePanelBlock(blocks.StructBlock):
    photo = ImageChooserBlock()
    text = blocks.RichTextBlock()


class HomePage(Page):
    body = RichTextField(blank=True)
    image_panels = StreamField([('ImagePanel', ImagePanelBlock())], blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        StreamFieldPanel('image_panels'),
    ]
