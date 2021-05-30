from django.urls import (
    path,
    re_path,
)
from .views import (
    CreateURLView,
    URLDetailView,
    URLRedirectView,
)


urlpatterns = [
    path('', CreateURLView.as_view(), name='home'),
    path('<int:pk>/', URLDetailView.as_view(), name='shortened_url'),
    re_path(r'^(?P<shortened_url>[a-zA-Z0-9]{8})/$', URLRedirectView.as_view(), name='url_redirect'),
]
