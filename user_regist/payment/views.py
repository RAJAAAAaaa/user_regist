from django.shortcuts import render
from .models import PaymentTxn
from django.http import HttpResponse
from .serializers import HistoryListingSerializer



response = HttpResponse()

def get_paymentTxn(request):
    pymtxn = PaymentTxn.objects.all()
    return render(request, {'pymtxn': pymtxn})


def pymt_filter(request):
    pymtxn = PaymentTxn.objects.filter(payment_id=id).first()
    return render(request, {'pymtxn': pymtxn})


def history(self, request):
    if request.method == "POST":
        user = request.user
        serializer_class = HistoryListingSerializer
        pymtxn_id = request.POST['pymtxn_id']
        pymtxn = PaymentTxn.objects.filter(user=user)
        queryset = PaymentTxn.history.filter(history_user=request.user)
        data = self.serializer_class(queryset, many=True).data
        history.save()
        return response(data)




