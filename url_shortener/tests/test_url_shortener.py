from django.db import IntegrityError
import pytest

from url_shortener.models import URL


# ------------------------------- FIKSTURY ---------------------------------------


@pytest.fixture
def url_object(db):
    """Tworzy obiekt URL."""

    URL.objects.create(shortened_url='gmaps', original_url='https://www.google.pl/maps', id=1)
    try:
        URL.objects.create(shortened_url='gmaps', original_url='https://www.google.pl/maps')
    except IntegrityError:
        pass


# ------------------------------- TESTY -----------------------------------------


def test_shortened_urls_are_unique(url_object):
    """Obiekty URL o identycznym `shortened_url` są niedozwolone."""
    with pytest.raises(IntegrityError):
        URL.objects.create(shortened_url='gmaps', original_url='https://www.google.pl/')


def test_original_url_duplicates_allowed(url_object):
    """Obiekty URL o identycznym `original_url` są dozwolone."""
    original_url = 'https://www.google.pl/maps'
    URL.objects.create(shortened_url='abcdefgh', original_url=original_url)
    assert URL.objects.filter(original_url=original_url).count() == 2
