from datetime import datetime
from django.shortcuts import render


def all_rooms(request):
    now = datetime.now()
    hungry = True
    return render(request, "all_rooms.htm", context={"now": now, "hungry": hungry})
