import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Operation
from .forms import OperationForm


def index (request):
    operation_list = Operation.objects.all()
    total = 0
    for operation in operation_list:
        total += operation.operation_summa
    context = {'operation_list': operation_list, 'total': total}
    return render(request, 'polls/index.html', context)

def operation_new(request):
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            operation = form.save(commit=False) 
            operation.operation_date = timezone.now()
            operation.save()
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = OperationForm()
    return render(request, 'polls/operation.html', {'form': form})
