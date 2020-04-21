from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path

from hello.views import get_tkb_ptit

admin.autodiscover()

urlpatterns = [
    re_path('tkb/(?P<type>\w+)/', get_tkb_ptit),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
