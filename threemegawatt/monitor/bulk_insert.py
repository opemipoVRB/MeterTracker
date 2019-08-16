#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
↓↓...........................................................................↓↓
↓↓..........................↓↓↓↓↓↓↓↓↓↓↓↓↓....................................↓↓
↓↓.......................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.................................↓↓
↓↓.....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓...............................↓↓
↓↓....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.↓↓...............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓...↓↓..............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.↓↓...↓↓↓.............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..............................↓↓
↓↓....................↓↓↓↓↓↓↓↓↓↓↓↓↓.....↓↓↓↓↓↓↓↓↓............................↓↓
↓↓......................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..↓↓↓↓↓↓↓............................↓↓
↓↓...................................↓↓↓.....................................↓↓
↓↓.................↓↓................↓↓↓↓ ↓↓↓↓↓↓↓........↓...................↓↓
↓↓...............↓↓↓↓↓↓..............↓↓↓↓↓↓↓↓↓↓↓↓↓...↓↓↓↓↓↓..................↓↓
↓↓............↓↓↓↓..↓↓↓↓↓.........................↓↓↓↓↓↓↓↓↓..................↓↓
↓↓............↓↓↓↓...↓↓↓↓↓↓↓....................↓↓↓↓↓↓.↓↓.↓↓.................↓↓
↓↓...............↓↓↓↓↓↓↓↓↓↓↓↓↓↓............↓↓↓↓↓↓↓↓..........................↓↓
↓↓.........................↓↓↓↓↓↓↓↓↓...↓↓↓↓↓↓↓...............................↓↓
↓↓..............................↓↓↓↓↓↓↓↓↓↓...................................↓↓
↓↓..........................↓↓↓↓↓....↓↓↓↓↓↓↓↓↓...............................↓↓
↓↓............↓↓.↓↓↓↓↓↓↓↓↓↓↓↓↓............↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..................↓↓
↓↓............↓↓.↓↓..↓↓↓↓.....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓.................↓↓
↓↓..............↓↓↓↓↓↓............................↓↓.↓↓↓↓↓↓↓.................↓↓
↓↓..................                                   ......................↓↓
↓↓.................. ↑↑↑  ↑↑↑  ↑↑↑↑↑↑↑        ↑↑↑↑↑↑↑ .......................↓↓
↓↓.................. ↑↑↑  ↑↑↑  ↑↑↑   ↑↑↑↑     ↑↑↑   ↑↑↑↑.....................↓↓
↓↓.................. ↑↑↨  ↑↑↑  ↑↑↨   ↨↑↑      ↑↑↨   ↨↑↑......................↓↓
↓↓.................. ↨↑↨  ↑↨↑  ↨↑↨   ↨↑↨      ↨↑↨   ↨↑↨......................↓↓
↓↓.................. ↑↨↑  ↨↑↨  ↨↨↑↨↑↨↨↑↑↨     ↨↨↑↨↑↨↨↑↑↨.....................↓↓
↓↓.................. ↨↑↨  ↨↨↨  ↨↨↨      ↨↨↨   ↨↨↨     ↨↨↨....................↓↓
↓↓.................. :↨:  ↨↨:  ↨↨:      :↨↨   ↨↨:     :::....................↓↓
↓↓................... ::↨↨:↨   :↨:      :↨:   :↨:     :::....................↓↓
↓↓.................... ::::    :::      :::   :::     :::....................↓↓
↓↓...................... :      :        :      :::::::  ....................↓↓
↓↓...........................................................................↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓      bulk_insert.py  Created by  Durodola Opemipo 2019                    ↓↓
↓↓            Personal Email : <opemipodurodola@gmail.com>                   ↓↓
↓↓                 Telephone Number: +2348182104309                          ↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓

"""
import json
import time
import uuid

import requests

import pandas as pd
from collections import defaultdict
from django.apps import apps


# plant_id = "Alpha"
# _from_ = "2018-01-01"
# _to_ = "2019-02-01"


def get_data_points(_plant_id, _from_, _to_):
    """
    Gets data points from the plant and presents it in a way that suits the schema of the db table data point
    :param _plant_id:
    :param _from_:
    :param _to_:
    :return:
    """
    # put url in env file
    url = "http://localhost:5000/?plant-id=" + _plant_id + "&from=" + _from_ + "&to=" + _to_
    response = requests.get(url).json()

    return response


def format_data_points(_plant_id, datapoints):
    """
    This Restructures the dataset to fit datapoint model

    :param _plant_id:
    :param datapoints:
    :return:
    """
    # Using Pandas Dataframe
    df = pd.DataFrame(list(datapoints))
    try:
        date_time = df.datetime.tolist()

        # Extract columns
        # Convert columns observed and expected to extract data energ and irradiation
        observed = df.observed.tolist()
        expected = df.expected.tolist()
        dfo = pd.DataFrame(observed)
        dfe = pd.DataFrame(expected)
        # Extracted columns to be merged in a new data_frame
        energy_expected = dfe.energy.tolist()
        irradiation_expected = dfe.irradiation.tolist()
        energy_observed = dfo.energy.tolist()
        irradiation_observed = dfo.irradiation.tolist()
        plant = [_plant_id for i in range(len(datapoints))]
        # pk = [uuid.uuid4() for i in range(len(datapoints))]
        # print(id)
        columns = ['energy_expected', 'energy_observed', 'irradiation_expected', 'irradiation_observed',
                   'datetime',
                   'plant']
        values = [energy_expected, energy_observed, irradiation_expected, irradiation_observed, date_time, plant]
        # columns = ['pk', 'energy_expected', 'energy_observed', 'irradiation_expected', 'irradiation_observed',
        #            'datetime',
        #            'plant']
        # values = [pk, energy_expected, energy_observed, irradiation_expected, irradiation_observed, date_time, plant]
        # Transposing data
        transpose = list(map(list, zip(*values)))
        clean_data = [dict(zip(columns, items)) for items in transpose]
    except AttributeError:
        return None

    return clean_data


class DataSetCreateManager:
    """

    This helper class keeps track of ORM objects to be created for multiple
    model classes, and automatically creates those objects with `bulk_create`
    when the number of objects accumulated for a given model class exceeds
    `batch_size`.
    Upon completion of the loop that's `add()`ing objects, the developer must
    call `done()` to ensure the final set of objects is created for all models.


    """

    def __init__(self, batch_size=1000):
        self._create_queues = defaultdict(list)
        self.batch_size = batch_size

    def _commit(self, custom_model):
        column_name = custom_model._meta.label
        custom_model.objects.bulk_create(self._create_queues[column_name])
        self._create_queues[column_name] = []

    def add(self, obj):
        """
        Add an object to the queue to be created, and call bulk_create if we
        have enough objs.
        """
        custom_model = type(obj)
        column_name = custom_model._meta.label
        self._create_queues[column_name].append(obj)
        if len(self._create_queues[column_name]) >= self.batch_size:
            self._commit(custom_model)

    def done(self):
        """
        Always call this upon completion to make sure the final partial chunk
        is saved.
        """
        for custom_model, objs in self._create_queues.items():
            if len(objs) > 0:
                self._commit(apps.get_model(custom_model))
