from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    RedirectView,
)
from .forms import URLForm
from .models import URL


class CreateURLView(CreateView):
    """Widok zawierający formularz do generowania skróconych URLi."""

    form_class = URLForm
    model = URL
    template_name = 'home.html'

    def get_success_url(self):
        return reverse('shortened_url', kwargs={'pk': self.object.pk})


class URLDetailView(DetailView):
    """Widok zawierający szczegóły dot. utworzonego skróconego URLa."""

    model = URL
    template_name = 'detail.html'


class URLRedirectView(RedirectView):
    """Widok przekierowujący do oryginalnego URLa na podstawie skróconego URLa."""

    def get_redirect_url(self, *args, **kwargs):
        return get_object_or_404(URL, shortened_url=kwargs['shortened_url']).original_url
