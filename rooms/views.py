from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = int(request.GET.get("page"))
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=6)
    rooms = paginator.get_page(page)  # rooms는 <class 'django.core.paginator.Page'>
    print(type(rooms))
    return render(
        request,
        "rooms/home.html",
        context={"page": rooms},
    )
