from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from models.models.partners import Partner


class HomeViewSet(viewsets.ModelViewSet):
    model = Partner
    http_method_names = ["get", "head"]

    def get_queryset(self):
        fields = self.request.GET.copy()
        return self.model.objects.filter(**fields.dict())

    def list(self, request, *args, **kwargs):
        return render(request, 'index.html')
