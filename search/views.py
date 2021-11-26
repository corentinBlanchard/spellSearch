from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404

from .models import Classes, Monster, Sorts
from .forms import SearchForm


def search(response):

    render_sorts_list = []
    if(response.method == "POST"):
        form = SearchForm(response.POST, response.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            sorts_list = Sorts.objects.filter(name__contains = data["name"])
            if data["is_verbal"]:
                sorts_list = sorts_list.filter(is_verbal = True)
            if data["is_somatic"]:
                sorts_list = sorts_list.filter(is_somatic = True)
            if data["is_material"]:
                sorts_list = sorts_list.filter(is_material = True)
            sorts_list = sorts_list.filter(max_level__lte = data["max_level"])

            
    else : 

        sorts_list = Sorts.objects.all()
        
    form = SearchForm()
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
        

    return render(response, "../templates/search/search.html", {"sorts_list": render_sorts_list, "form": form})