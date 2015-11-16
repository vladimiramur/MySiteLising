from django.db import models


class Operation(models.Model):
    operation_text = models.CharField(max_length=100)
    operation_date = models.DateField('date operation')
    operation_summa = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.operation_text
