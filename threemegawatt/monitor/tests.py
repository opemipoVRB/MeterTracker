import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Plant, DataPoint


# initialize the APIClient app


# Create your tests here.


class PlantModelTestCase(TestCase):
    """
    Test Case for Plant model

    """

    def setUp(self):
        Plant.objects.create(
            name='Alpha Plant'
        )
        Plant.objects.create(
            name='Beta Plant'
        )

    def test_get_all_plant(self):
        alpha_plant = Plant.objects.get(name='Alpha Plant')
        beta_plant = Plant.objects.get(name='Beta Plant')

        self.assertIsInstance(alpha_plant, Plant)
        self.assertIsInstance(beta_plant, Plant)
        self.assertEqual(alpha_plant.name, "Alpha Plant")
        self.assertEqual(beta_plant.name, "Beta Plant")


class PlantsViewTestCase(TestCase):
    """
    Test module for Get all API

    """

    def setUp(self):
        """
        Defining test client and test variables

        :return:
        """
        self.client = APIClient()
        self.plant = {'name': 'Alpha Plant'}
        self.response = self.client.post(
            reverse('plant-create'),
            self.plant,
            format='json')

    def test_api_can_create_plant(self):
        """

        Test the API create plant

        :return:
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_all_plant(self):
        """

        Test the API get all plant

        :return:

        """
        plant = Plant.objects.get()

        response = self.client.get(
            reverse('plant-list',
                    ),
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(
            response,
            plant
        )

    def test_api_get_can_a_plant(self):
        """
        Test the api can get a given plant
        :return:

        """

        plant = Plant.objects.get()

        response = self.client.get(
            reverse('plant-detail',
                    kwargs={'pk': plant.id}),
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertContains(
            response,
            plant
        )

    def test_api_can_update_a_plant(self):
        """
                Test the api can put/update a given plant

        :return:
        """
        plant = Plant.objects.get()

        plant_update = {
            'name': 'Omega Plant'
        }

        response = self.client.put(
            reverse('plant-update', kwargs={'pk': plant.id}),
            plant_update, format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_api_can_delete_plant(self):
        """
        Test the api can delete a plant

        :return:
        """
        plant = Plant.objects.get()

        response = self.client.delete(
            reverse('plant-delete', kwargs={'pk': plant.id}),
            format='json',
            follow=True
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class DataPointModelTestCase(TestCase):
    """
    Test Case for DataPoint model

    """

    def setUp(self):
        self.plant = Plant.objects.create(
            name='Alpha Plant'
        )

        self.current_timezone = timezone.get_current_timezone()

        self.data_point_1 = DataPoint.objects.create(
            plant_id=self.plant.id,
            energy_expected=87.55317774223157,
            energy_observed=90.78559770167864,
            irradiation_expected=98.19878838432548,
            irradiation_observed=30.085498370965905,
            datetime=self.current_timezone.localize(datetime.datetime.strptime('2019-01-01T00:00:00',
                                                                               '%Y-%m-%dT%H:%M:%S')),

        )

        self.data_point_2 = DataPoint.objects.create(
            plant_id=self.plant.id,
            energy_expected=87.55317774223157,
            energy_observed=90.78559770167864,
            irradiation_expected=98.19878838432548,
            irradiation_observed=30.085498370965905,
            datetime=self.current_timezone.localize(datetime.datetime.strptime('2019-01-01T01:00:00',
                                                                               '%Y-%m-%dT%H:%M:%S')),
        )

    def test_get_all_data_points(self):
        data_point_1 = DataPoint.objects.get(id=self.data_point_1.id)
        data_point_2 = DataPoint.objects.get(id=self.data_point_2.id)

        self.assertIsInstance(self.plant, Plant)
        self.assertIsInstance(data_point_1, DataPoint)
        self.assertIsInstance(data_point_2, DataPoint)


class DataPointViewTestCase(TestCase):
    """
    Test module for Get all API

    """

    def setUp(self):
        """
        Defining test client and test variables

        :return:
        """

        self.plant = Plant.objects.create(
            name='Alpha Plant'
        )

        self.client = APIClient()
        date_from = "2019-01-01"
        date_to = "2019-02-01"
        self.response = self.client.post(
            reverse('bulk-upload-datapoints'),
            {
                'plant': self.plant.id,
                'date_from': date_from,
                'date_to': date_to
            }
            ,
            format='json'
        )

    def test_api_can_create_data_points(self):
        """
        Test the API create bulk upload returns a 204 if there is no content

        :return:


        """

        if status.HTTP_201_CREATED == self.response.status_code:
            self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        else:
            self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_generate_report(self):
        """
        Test the api can get data points from  a given date range to generate report

        :return:

        """

        plant_id = str(self.plant.id)

        datapoint = DataPoint.objects.filter(plant=plant_id)

        response = self.client.get(
            reverse(
                'generate-plant-report',
                kwargs={'plant': plant_id}
            ),
            format='json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )