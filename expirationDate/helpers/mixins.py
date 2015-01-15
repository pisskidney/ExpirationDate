from django.db import models


class WithImageMixin(models.Model):
    image = models.ImageField(null=True)

    class Meta():
        abstract = True

    def render_image(self):
        # Do not do this in production
        if self.image:
            return u'<img src="{}" style="width:128px !important"/>'.format(
                self.image.url)
        else:
            return '(No image)'
    render_image.short_description = 'Image preview'
    render_image.allow_tags = True
