from django.views.generic import ListView
from . import models
from django.core.paginator import Page


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 6
    ordering = "id"
