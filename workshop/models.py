from django.db import models
from users.models import AppUser


class Part(models.Model):
    name = models.CharField(max_length=256)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    available = models.PositiveIntegerField()

    def __str__(self):
        return f"Деталь {self.name}"


class Service(models.Model):
    name = models.CharField(max_length=256)
    cost = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Услуга {self.name}"



class Order(models.Model):
    worker = models.ForeignKey(AppUser,
                              related_name="orders",
                              on_delete=models.CASCADE,
                              verbose_name="Работник принявший заказ")

    on_work = models.BooleanField(default=False)
    is_ready = models.BooleanField(default=False)
    client_name = models.CharField(max_length=256)
    client_phone_number = models.CharField(max_length=10)
    date = models.DateField()
    date_ready = models.DateField()
    #photo = models.ImageField()
    description = models.TextField()



class PartsOfOrder(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name="parts_in_orders")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="parts_in_orders")
    amount = models.PositiveIntegerField()


class ServicesOfOrder(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name="services_in_orders")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="services_in_orders")
    amount = models.PositiveIntegerField()


class CustomService(models.Model):
    name = models.CharField(max_length=256)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="custom_services_in_orders")

