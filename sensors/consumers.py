# sensors/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json

from django.core.exceptions import ObjectDoesNotExist

from sensors.models import Sensors


class SensorConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        sensor_list = {}
        for sensor in Sensors.objects.all():
            try:
                value = str(sensor.measurements_set.latest().value)+" "+sensor.unit
            except ObjectDoesNotExist:
                value = "N/A"
            sensor_list[sensor.id] = value

        self.send(text_data=json.dumps(sensor_list))
