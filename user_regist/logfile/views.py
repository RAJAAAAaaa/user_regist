from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .serializers import HistoryListingSerializer

response = HttpResponse()


def history_log(self, request):
    serializer_class = HistoryListingSerializer
    queryset = Log.history.filter(history_user=request.user)
    data = self.serializer_class(queryset, many=True).data
    return response(data)

