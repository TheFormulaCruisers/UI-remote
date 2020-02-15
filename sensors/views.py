from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Sensors


def index(request):
    sensor_list = []
    for sensor in Sensors.objects.all():
        try:
            value = sensor.measurements_set.latest().value
        except ObjectDoesNotExist:
            value = None

        sensor_list.append({
            'id': sensor.id,
            'name': sensor.name,
            'value': value,
            'unit': sensor.unit
        })

    return render(request, 'dashboard.html', locals())


def sensor(request, sensor_id):
    sensor = Sensors.objects.get(id=sensor_id)
    latest_measurements = sensor.measurements_set.all().order_by('-measure_time')[:10]
    return render(request, 'sensor.html', locals())
