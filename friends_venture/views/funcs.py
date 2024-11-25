from django.http import HttpResponse
from django.shortcuts import render, redirect
from models.models.partners import Partner
from models.models.transactions import Transaction

import ipdb


from rest_framework.status import (
    HTTP_200_OK,
)


def health_check(request):
    return HttpResponse(status=HTTP_200_OK)


def home(request):
    return render(request, 'home/index.html')


def delete_partner(request, *args, **kwargs):
    try:
        pid = kwargs.get('id', 0)
        partner = Partner.objects.get(pk=pid)
    except Exception as e:
        print(e)
    else:
        partner.delete()
    return redirect('/partner')


def delete_transaction(request, *args, **kwargs):
    try:
        tid = kwargs.get('id', 0)
        partner = Transaction.objects.get(pk=tid)
    except Exception as e:
        print(e)
    else:
        partner.delete()
    return redirect('/transaction')
