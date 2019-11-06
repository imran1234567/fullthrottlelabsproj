from django.shortcuts import render
from .models import Search
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
# Create your views here.

class ProjectappDetailView(DetailView):
    queryset = Search.objects.all()


class ProjectappListView(ListView):    
    def get_queryset(self, *args, **kwargs):
        qs = Search.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(name__icontains=query) |
                    Q(custom_number__icontains=query)
                    )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectappListView, self).get_context_data(*args, **kwargs)
        return context


def search_detail_view(request, pk=None): # pk == id
    #obj = Tweet.objects.get(pk=pk) # GET from database
    obj = get_object_or_404(Search, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "projectapp/detail_view.html", context)