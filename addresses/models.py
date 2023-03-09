from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name='Локация', unique=True)

    def __str__(self):
        return self.name


class Datacenter(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Датацентр')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Network(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование сети')
    datacener = models.ForeignKey(Datacenter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Addresses(models.Model):
    addresses = models.CharField(max_length=15, unique=True, verbose_name='ip адрес')
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



