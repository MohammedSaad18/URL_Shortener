from django.db.models import Count
from .models import Click
from .serializers import ShortURLSerializer
import shorten
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from shorten.models import ShortURL


# Create your views here.
class ListShortURLs(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        #ShortURLs = ShortURL.objects.filter(author=request.user)
        ShortURLs = ShortURL.objects.all()
        serializer = ShortURLSerializer(ShortURLs, many=True)
        return Response(serializer.data)


class LinePlotAllURLS(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # clicks = Click.objects.all().filter(shorturl__author=request.user).values(
        #     'click_date').annotate(count=Count('id'))

        clicks = Click.objects.all().values(
            'click_date').annotate(count=Count('id'))

        data = []
        labels = []

        for click in clicks:
            data.append(click['count'])
            labels.append(click['click_date'])

        content = {'data': data, 'labels': labels}
        return Response(content)


class LinePlotURL(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, shortcode=None, *args, **kwargs):
        # clicks = Click.objects.all().filter(shorturl__author=request.user).values(
        #     'click_date').annotate(count=Count('id'))

        clicks = Click.objects.all().filter(shorturl__shortcode=shortcode).values(
            'click_date').annotate(count=Count('id'))

        data = []
        labels = []

        for click in clicks:
            data.append(click['count'])
            labels.append(click['click_date'])

        content = {'data': data, 'labels': labels}
        return Response(content)


class CountriesAllURLS(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # clicks = Click.objects.all().filter(shorturl__author=request.user).values(
        #     'click_date').annotate(count=Count('id'))

        clicks = Click.objects.all().values(
            'country').annotate(count=Count('id'))

        data = []
        labels = []

        for click in clicks:
            data.append(click['count'])
            labels.append(click['country'])

        content = {'data': data, 'labels': labels}
        return Response(content)


class CountriesURL(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, shortcode=None, *args, **kwargs):
        # clicks = Click.objects.all().filter(shorturl__author=request.user).values(
        #     'click_date').annotate(count=Count('id'))

        clicks = Click.objects.all().filter(shorturl__shortcode=shortcode).values(
            'country').annotate(count=Count('id'))

        data = []
        labels = []

        for click in clicks:
            data.append(click['count'])
            labels.append(click['country'])

        content = {'data': data, 'labels': labels}
        return Response(content)


class OsAllURLS(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # clicks = Click.objects.all().filter(shorturl__author=request.user).values(
        #     'click_date').annotate(count=Count('id'))

        clicks = Click.objects.all().values(
            'os').annotate(count=Count('id'))

        data = []
        labels = []

        for click in clicks:
            data.append(click['count'])
            labels.append(click['os'])

        content = {'data': data, 'labels': labels}
        return Response(content)


class OsURL(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, shortcode=None, *args, **kwargs):
        # clicks = Click.objects.all().filter(shorturl__author=request.user).values(
        #     'click_date').annotate(count=Count('id'))

        clicks = Click.objects.all().filter(shorturl__shortcode=shortcode).values(
            'os').annotate(count=Count('id'))

        data = []
        labels = []

        for click in clicks:
            data.append(click['count'])
            labels.append(click['os'])

        content = {'data': data, 'labels': labels}
        return Response(content)
# Click.objects.all().filter(shorturl__author=user).values('country').annotate(count=Count('id'))


class RefererURL(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, shortcode=None, *args, **kwargs):

        if shortcode is not None:
            clicks = Click.objects.all().filter(shorturl__shortcode=shortcode).values(
                'referer').annotate(count=Count('id'))
        else:
            clicks = Click.objects.all().values(
                'referer').annotate(count=Count('id'))
        data = []
        labels = []

        for click in clicks:
            data.append(click['count'])
            labels.append(click['referer'])

        content = {'data': data, 'labels': labels}
        return Response(content)


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
