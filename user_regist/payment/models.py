from django.db import models
from django.contrib.auth.models import User
from simple_history import register
from simple_history.models import HistoricalRecords


class PaymentTxn(models.Model):
    name = models.CharField(max_length=50)
    payment_id = models.AutoField(primary_ker=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True)),
    __history_date = None

