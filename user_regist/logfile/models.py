from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, redirect
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
import logging

old_log = logging.getLogRecordFactory()


class Log(models.model):

    user_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    createTime = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True)),

    def new_log(self, *args, **kwargs):
        record = old_log(*args, **kwargs)
        changed_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        return record

    logging.setLogRecordFactory(new_log)

