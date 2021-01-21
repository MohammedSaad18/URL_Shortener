from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Click
from django.db.models import Count


# Create your views here.

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