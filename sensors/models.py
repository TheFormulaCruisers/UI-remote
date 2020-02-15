from django.db import models


class Sensors(models.Model):
    node = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=30)
    description = models.CharField(max_length=30)
    unit = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'sensors'
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensors'


class Measurements(models.Model):
    measure_time = models.DateTimeField(primary_key=True)
    sensor = models.ForeignKey('Sensors', models.DO_NOTHING)
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'measurements'
        unique_together = (('measure_time', 'sensor'),)
        get_latest_by = 'measure_time'
        verbose_name = 'Measurement'
        verbose_name_plural = 'Measurements'

# class Sensors(models.Model):
#     name = models.CharField(unique=True, max_length=30)
#     description = models.CharField(max_length=30)
#     unit = models.CharField(max_length=5)
#
#     class Meta:
#         db_table = 'sensors'
#         verbose_name = 'Sensor'
#         verbose_name_plural = 'Sensors'
#
#
# class TempSensor(models.Model):
#     measure_time = models.DateTimeField(primary_key=True)
#     sensor = models.ForeignKey(Sensors, models.DO_NOTHING)
#     value = models.FloatField()
#
#     class Meta:
#         db_table = 'temp_sens'
#         verbose_name = 'Temperature Sensor Measurement'
#         verbose_name_plural = 'Temperature Sensor Measurements'
#
#     def __str__(self):
#         return f'{self.sensor.name}'
