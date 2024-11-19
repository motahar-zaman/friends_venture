import ipdb
from django.http import HttpResponse
from django.shortcuts import render, redirect
from models.models.partners import Partner


from rest_framework.status import (
    HTTP_200_OK,
)


def health_check(request):
    return HttpResponse(status=HTTP_200_OK)


def home(request):
    return render(request, 'home/index.html')


def delete_partner(request, *args, **kwargs):
    # ipdb.set_trace()
    try:
        pid = kwargs.get('id', 0)
        partner = Partner.objects.get(pk=pid)
    except Exception as e:
        print(e)
    else:
        partner.delete()
    return redirect('/partner')
