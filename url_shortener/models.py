"""Moduł zawierający modele używane w aplikacji URL Shortener."""
from django.db import models
import random
import string


SHORT_URL_CHARS = string.ascii_letters + string.digits


class URL(models.Model):
    """Przechowuje dane dotyczące skracanych adresów URL."""

    original_url = models.URLField('URL użytkownika')
    shortened_url = models.CharField('skrócony URL', unique=True, max_length=8)
    created_at = models.DateTimeField('utworzono', auto_now_add=True)
    updated_at = models.DateTimeField('zaktualizowano',auto_now=True)

    def __str__(self):
        return self.shortened_url

    class Meta:
        verbose_name = 'skrót adresu URL'
        verbose_name_plural = 'skróty adresów URL'

    def save(self, *args, **kwargs):
        if not self.shortened_url:
            self.shortened_url = self._get_random_url()
        super().save(*args, **kwargs)

    @classmethod
    def _get_random_url(cls):
        """Zwraca ciąg losowych znaków na potrzeby utworzenia skróconego urla."""
        shortened_url = ''.join(random.choice(SHORT_URL_CHARS) for _ in range(8))
        if not cls.objects.filter(shortened_url=shortened_url).exists():
            return shortened_url
        return cls._get_random_url()
