from django.db import models
from django.utils.translation import gettext_lazy as _

from filebrowser.fields import FileBrowseField

# Create your models here.


class Slide(models.Model):
    title = models.CharField(_('slide title'), max_length=255)
    subtitle = models.TextField(_('slide subtitle'))
    image = FileBrowseField(
        _('slide image'),
        max_length=255,
        directory='slides/',
        extensions=['.jpg', '.jpeg', '.png'],
    )

    class Meta:
        verbose_name = _('slide')
        verbose_name_plural = _('slides')

    def __str__(self):
        return self.title
