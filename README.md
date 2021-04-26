# Hallo.js not fully working

When upgrading to Wagtail 2.13rc1, I discovered text was not rendered in the
Hallo.js rich text area. While building this repository, I found that the rich
text editor behaves as expected if used in a StreamField - but not when the rich
text block is used as part of a StructBlock.

This works as expected. After saving a draft, the text saved in the body field
is available in the rich text editor for further editing.
```
class HomePage(Page):
    body = RichTextField(blank=True)
```

But this does not:
```
class ImagePanelBlock(blocks.StructBlock):
    photo = ImageChooserBlock()
    text = blocks.RichTextBlock()
```

One can add text to the field and it previews just fine. But after saving a
draft or publishing, when you return to the editor, the text from the database
is not available inside the editor window - even though the page preview shows
the text is still available for rendering.

!['Editor interface vs. preview of same'](https://github.com/cnk/hallo-issue/blob/main/HalloJSNotShowingText.png?raw=true)

