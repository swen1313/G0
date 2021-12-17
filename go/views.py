from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

side_dict = {
    'nord':'север.там холодно',
    'sud':'юг.там жарко',
    'west':'запад.там солнце садится',
    'east':'восток.там солнце встает'

}

def main(request):
    result=" "
    for i in side_dict.keys():
        re_url = reverse("name", args=(i,))
        result += f"<li><a href='{re_url}'>{i.title()}</a></li>"

    return HttpResponse(result)





def get_redirect(request):
    return HttpResponseRedirect("/go/nord")

def get_side(request, side):
    side_values = side_dict.get(side, None)
    if side_values:
        return HttpResponse(side_values)
    else:
        return HttpResponseNotFound(f'нет такого{side}')







# Create your views here.
