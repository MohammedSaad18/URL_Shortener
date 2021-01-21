from rest_framework import serializers

Click.objects.values('click_date').annotate(count=Count('id'))
