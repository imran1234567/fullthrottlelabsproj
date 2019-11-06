from django.urls import path, re_path
from .views import ProjectappListView, search_detail_view


urlpatterns = [
    path('', ProjectappListView.as_view(), name='list'),
    re_path(r'^(?P<pk>\d+)/$', search_detail_view, name='detail')
]
