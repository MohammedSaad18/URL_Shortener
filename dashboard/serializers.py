from rest_framework import serializers


class ShortURLSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=200)
    shortcode = serializers.CharField(
        max_length=15,   allow_blank=True)
    created_at = serializers.DateTimeField()
