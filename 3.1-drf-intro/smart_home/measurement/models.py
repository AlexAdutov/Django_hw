from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'Sensor_{self.sensor}_{self.created_at}'