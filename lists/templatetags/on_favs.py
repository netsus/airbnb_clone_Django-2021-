from django import template
from lists import models as list_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, room):
    # request = context.get("request")
    user = context.request.user
    the_list = list_models.List.objects.get_or_none(
        user=user, name="My Favorites Houses"
    )
    # print(room in the_list.rooms.all())
    return room in the_list.rooms.all()
