# This file only serves to represent the necessary fields for the requests to the beer endpoints.
# It is only for using Swagger, in another scenario Swagger is neither developed nor included

from rest_framework import serializers

class RequestBeerSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()
