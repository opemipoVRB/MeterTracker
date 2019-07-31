from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Plant
from .serializers import PlantSerializer


# Create your views here.


class PlantViewSet(viewsets.ModelViewSet):
    """
        ViewSet for Plant model provides
        list, create, retrieve, update, partial_update,destroy

    """

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


plant_list = PlantViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

plant_detail = PlantViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# class PlantViewSet(viewsets.ViewSet):
#     """
#             API VIew for Plant model
#
#     """
#
#     def list(self, request):
#         """
#         List all existing plant
#
#         :param request:
#         :return:
#         """
#         queryset = Plant.objects.all()
#         serializer = PlantSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         """
#         Retrieve object with an id
#
#         :param request:
#         :param pk:
#         :return:
#         """
#
#         queryset = Plant.objects.all()
#         plant = get_object_or_404(queryset, pk=pk)
#         serializer = PlantSerializer(plant, many=True)
#         return Response(serializer.data)
#
#
#
#
#
#     def create(self, request):
#         """
#         Create a new plant object
#
#         :param request:
#         :return:
#         """
#
#         serializer_class = PlantSerializer
#         #
#         # if serializers.is_valid():
#         #     name = serializers.data.get('name')
#         #     message = ""
#
#         pass
