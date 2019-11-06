from rest_framework import generics
from projectapp.models import Search
from .serializers import SearchModelSerializers

class SearchListAPIView(generics.ListAPIView):
    serializer_class = SearchModelSerializers

    def get_queryset(self):
        return Search.objects.all()
