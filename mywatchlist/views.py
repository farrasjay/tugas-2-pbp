from django.shortcuts import render
from mywatchlist.models import watchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_watchlist(request):
    data_watchlist = watchList.objects.all()
    context = {
        'watchlist': data_watchlist,
        'nama': 'Farras Hafizhudin Indra Wijaya',
        'npm' : '2106652682'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = serializers.serialize("xml", watchList.objects.all())
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    data = serializers.serialize("json", watchList.objects.all())
    return HttpResponse(data, content_type="application/json")

def show_html_by_id(request, id):
    data_watchlist = watchList.objects.filter(pk=id)
    context = {
        'watchlist': data_watchlist,
        'nama': 'Farras Hafizhudin Indra Wijaya',
        'npm' : '2106652682'
    }
    return render(request, "mywatchlist.html", context)

def show_json_by_id(request, id):
    data = watchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id) :
    data = watchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")