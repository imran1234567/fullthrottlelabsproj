from django.db.models import Q
from rest_framework import generics
from projectapp.models import Search
from .serializers import SearchModelSerializers

class SearchListAPIView(generics.ListAPIView):
    serializer_class = SearchModelSerializers

    def get_queryset(self, *args, **kwargs):
        qs = Search.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(name__icontains=query) |
                    Q(custom_number__icontains=query)
                    )
        return qs
