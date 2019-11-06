from django.urls import path, re_path
from django.views.generic.base import RedirectView

from .views import SearchListAPIView

urlpatterns = [
    path('', SearchListAPIView.as_view(), name='list' )
]
