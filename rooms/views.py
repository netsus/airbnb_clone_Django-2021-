from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=6)
    try:
        rooms = paginator.page(int(page))  # rooms는 <class 'django.core.paginator.Page'>
        return render(request, "rooms/home.html", context={"page": rooms})
    except EmptyPage:
        return redirect("/")
