from django.db import models
from django.utils.translation import gettext_lazy as _

from filebrowser.fields import FileBrowseField

# Create your models here.


class Company(models.Model):
    name = models.CharField(_('company name'), max_length=255)
    logo = FileBrowseField(
        _('company logo'), max_length=255, directory='company/', extensions=['.png']
    )

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('company')

    def __str__(self):
        return self.name
