from django.test import TestCase
from django.urls import reverse
# from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Plant, Datapoint


# initialize the APIClient app


# Create your tests here.


class PlantTestCase(TestCase):
    """
    Test Case for Puppy model

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
            reverse('plant-list'),
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

    def test_api_can_update_plant(self):
        """

        :return:
        """
        plant = Plant.objects.get()

        plant_update = {
            'name': 'Omega Plant'
        }

        response = self.client.put(
            reverse('plant-detail', kwargs={'pk': plant.id}),
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
            reverse('plant-detail', kwargs={'pk': plant.id}),
            format='json',
            follow=True
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


