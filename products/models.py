from django.db import models
from django.utils.translation import gettext_lazy as _

from filebrowser.fields import FileBrowseField

# Create your models here.


class Product(models.Model):
    class Category(models.TextChoices):
        ACTIVE = 'AC', _('Active')
        WIRELESS = 'WI', _('Wireless')
        CCTV = 'CC', _('Camera')
        POWER = 'PO', _('Power & Earth')
        TOWER = 'TO', _('Tower')

    title = models.CharField(_('product title'), max_length=255)
    category = models.CharField(
        _('product category'), choices=Category.choices, max_length=2
    )
    image = FileBrowseField(
        _('product image'),
        max_length=255,
        directory='products/',
        extensions=['.jpg', '.jpeg', '.png'],
    )
