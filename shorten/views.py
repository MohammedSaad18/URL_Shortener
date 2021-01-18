from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import ShortURL
from .serializers import ShortURLSerializer
from .forms import ShortenURLForm
from dashboard.models import Click
from django.views.generic import View
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from user_agents import parse

"""
def home(request):

    if request.method == "POST":
        form  = ShortenURLForm(request.POST)
        if form.is_valid():
            obj_url =  form.cleaned_data.get("url")
            if request.user.is_authenticated:
                shorturl = ShortURL(url = obj_url , author = request.user )
            else:
                 shorturl = ShortURL(url = obj_url)
            shorturl.save()
    else:
        form  = ShortenURLForm()
    context= {
        'form' : form
    }
    return render(request, 'shorten/home.html' , context)
"""


def home(request):

    form = ShortenURLForm(request.POST or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            obj_url = form.cleaned_data.get("url")
            if request.user.is_authenticated:
                shorturl = ShortURL(url=obj_url, author=request.user)
            else:
                shorturl = ShortURL(url=obj_url)
            shorturl.save()
            data['shorturl'] = shorturl.get_absolute_url()

            return JsonResponse(data)

    context = {
        'form': form
    }

    return render(request, 'shorten/home.html', context)


class ListShortURLs(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        #ShortURLs = ShortURL.objects.filter(author=request.user)
        ShortURLs = ShortURL.objects.all()
        serializer = ShortURLSerializer(ShortURLs, many=True)
        return Response(serializer.data)


class Home_view(View):

    def get(self, request, *args, **kwargs):
        form = ShortenURLForm()
        context = {
            'form': form
        }
        return render(request, 'shorten/home.html', context)

    def post(self, request, *args, **kwargs):
        form = ShortenURLForm(request.POST)
        shortcode = None
        if form.is_valid():
            obj_url = form.cleaned_data.get("url")
            if request.user.is_authenticated:
                shorturl = ShortURL(url=obj_url, author=request.user)
            else:
                shorturl = ShortURL(url=obj_url)
            shorturl.save()
            shortcode = shorturl.shortcode

        context = {
            'form': form,
            'shortcode': shortcode
        }
        return render(request, 'shorten/home.html', context)


def short_url_redirect(request, shortcode=None):
    obj = get_object_or_404(ShortURL, shortcode=shortcode)
    obj_url = obj.url
    print('-----------------------------------------------')
    print(request.META.get('HTTP_REFERER'))
    print(request.COUNTRY_CODE)

    agent = request.META["HTTP_USER_AGENT"]
    user_agent = parse(agent)
    os = user_agent.os.family

    clcik = Click(country=request.COUNTRY_CODE,
                  referer=request.META.get('HTTP_REFERER'), os=os, shorturl=obj)
    clcik.save()
    return HttpResponseRedirect(obj_url)
    # return HttpResponse("short = {sc} , user = {usr} , url = {url}".format(sc=shortcode, usr = request.user , url = obj_url))
