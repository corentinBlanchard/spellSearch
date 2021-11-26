from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404

from .models import Classes, Monster, Sorts

def search(response):
    sorts_list = Sorts.objects.all()
    render_sorts_list = []
    for sort in sorts_list:
        component = ""
        classes = ""
        monsters = ""

        if sort.is_verbal :
            component += "V "
        if sort.is_somatic :
            component += "S "
        if sort.is_material :
            component += "M "

        for c in Classes.objects.filter(sorts=sort):
            classes += c.name + " "

        for m in Monster.objects.filter(sorts=sort):
            monsters += m.name + " "


        thisdict =	{
            "name": sort.name,
            "components": component,
            "max_level": sort.max_level,
            "classes": classes,
            "monsters": monsters
            }
        render_sorts_list.append(thisdict)
        

    return render(response, "../templates/search/search.html", {"sorts_list": render_sorts_list})