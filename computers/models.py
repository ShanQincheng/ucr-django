from django.db import models


class Computer(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    picture = models.URLField()
    rent = models.FloatField()
    stocks = models.IntegerField(default=0)
    os = models.CharField(max_length=200, blank=True)
    DISP_size = models.IntegerField(default=13, blank=True)
    RAM = models.IntegerField(default=4, blank=True)
    USB_port_num = models.IntegerField(default=4, blank=True)
    HDMI_port_num = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name + " " + self.brand

    def was_out_of_stock(self):
        return self.stocks <= 0

