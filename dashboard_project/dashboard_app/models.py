from django.db import models

# dashboard_app/models.py

from django.db import models

class ExcelData(models.Model):
    # Definicja pól modelu do przechowywania danych z excela
    column1 = models.CharField(max_length=100)
    column2 = models.IntegerField()
    # Dodaj pola zgodnie z danymi, które chcesz przechowywać
