from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from .models import ShortURL
from .forms import ShortenURLForm
from django.views.generic import View
# Create your views here.

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

    form  = ShortenURLForm(request.POST or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            obj_url =  form.cleaned_data.get("url")
            shortcode = form.cleaned_data.get("shortcode")

            if request.user.is_authenticated:
                shorturl = ShortURL(url = obj_url, shortcode = shortcode, author = request.user )
            else:
                shorturl = ShortURL(url = obj_url, shortcode = shortcode)
            try:
                shorturl.save()
                data['shorturl'] = shorturl.get_absolute_url(request.get_host())
            except Exception as e:
               return HttpResponseBadRequest(e)

        return JsonResponse(data)

    context= {
        'form' : form
    }
    return render(request, 'shorten/home.html' , context)


class Home_view(View):

    def get(self, request, *args, **kwargs):
        form  = ShortenURLForm()
        context= {
            'form' : form   
        }
        return render(request, 'shorten/home.html' , context)

    def post(self, request, *args, **kwargs):
        form  = ShortenURLForm(request.POST)
        shortcode = None;
        if form.is_valid():
            obj_url =  form.cleaned_data.get("url")
            if request.user.is_authenticated:
                shorturl = ShortURL(url = obj_url , author = request.user )
            else:
                 shorturl = ShortURL(url = obj_url)
            shorturl.save()
            shortcode = shorturl.shortcode

        context= {
            'form' : form,
            'shortcode': shortcode  
        }
        return render(request, 'shorten/home.html' , context)

def short_url_redirect(request,shortcode=None):
    obj = get_object_or_404(ShortURL, shortcode = shortcode)
    obj_url = obj.url
    return HttpResponseRedirect(obj_url)


