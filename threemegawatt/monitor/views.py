import datetime
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from .bulk_insert import format_data_points, get_data_points, DataSetCreateManager
from .models import Plant, DataPoint
from .serializers import PlantSerializer, DataSetSerializer, DataPointSerializer


class APIRoot(generics.GenericAPIView):
    """
        3MegaWatt API documentation

    """


class PlantListView(ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantDetailView(RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantDestroyView(DestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantCreateView(CreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantUpdateView(RetrieveUpdateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class DataPointMixin(CreateModelMixin):

    """

    Mixin for bulk create and update operations.
    Either create a single or many model instances in bulk by using the
    Serializers ``many=True`` ability from Django REST >= 2.2.5.
    This mixin uses the same method to create model instances
    as ``CreateModelMixin`` because both non-bulk and bulk
    requests will use ``POST`` request method.



    """

    def create(self, request, *args, **kwargs):
        plant = request.data.get('plant')
        date_from = request.data.get('date_from')
        date_to = request.data.get('date_to')
        data = format_data_points(plant, get_data_points(plant, date_from, date_to))

        bulk = isinstance(data, list)

        current_timezone = timezone.get_current_timezone()

        if not bulk:
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            dataset_mgr = DataSetCreateManager(batch_size=1000)
            for obj in data:
                dataset_mgr.add(DataPoint(energy_expected=obj['energy_expected'],
                                          energy_observed=obj['energy_observed'],
                                          irradiation_expected=obj['irradiation_expected'],
                                          irradiation_observed=obj['irradiation_observed'],
                                          datetime=current_timezone.localize(datetime.datetime.strptime(obj['datetime'],
                                                                             '%Y-%m-%dT%H:%M:%S')),
                                          plant=Plant.objects.get(pk=obj['plant'])
                                          )
                                )

            dataset_mgr.done()
            return Response(status=status.HTTP_201_CREATED)

    def perform_bulk_create(self, serializer):
        return self.perform_create(serializer)


class DataSetCreateView(CreateAPIView, DataPointMixin):

    """
    Api for Creating Datapoint and Generating Reports

    """

    queryset = DataPoint.objects.all()
    serializer_class = DataSetSerializer


class PlantDataPoints(ListAPIView):

    """
    Api for Creating Datapoint and Generating Reports

    """
    lookup_field = 'plant'
    serializer_class = DataPointSerializer

    def get_queryset(self):
        plant = self.kwargs['plant']
        return DataPoint.objects.filter(plant=plant)

