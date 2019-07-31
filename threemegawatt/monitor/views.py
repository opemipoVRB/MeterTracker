from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from . import serializers


# Create your views here.


class CreatePlantView(CreateAPIView):
    """

    API VIew for Plant model

    """

    serializer_class = serializers.PlantSerializer

    def get(self, request, format=None):
        """
        Returns a list of
        :param request:
        :param format:
        :return:
        """
        pass

    def post(self, serializer):
        """

        :param serializer:
        :return:
        """
        pass
