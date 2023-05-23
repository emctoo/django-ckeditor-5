from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article


class ArticleListView(ListView):
    """All articles."""

    model = Article
    paginate_by = 100


class ArticleDetailView(DetailView):
    """Article detail view."""

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        success_url = reverse("article-detail", kwargs={"pk": self.get_object().id})
        return HttpResponseRedirect(success_url)
