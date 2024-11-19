from rest_framework.response import Response
from django.shortcuts import render
from friends_venture.serealizers import PartnerSerializer
from models.models.partners import Partner
from rest_framework import viewsets

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST
)


class PartnerViewSet(viewsets.ModelViewSet):
    model = Partner
    serializer_class = PartnerSerializer
    http_method_names = ["get", "head", "post", "patch", "update", "delete"]

    def get_queryset(self):
        fields = self.request.GET.copy()
        return self.model.objects.filter(**fields.dict())

    def retrieve(self, request, *args, **kwargs):
        store_configuration = self.get_object()
        serializer = self.serializer_class(store_configuration, context={"request": request})
        # return Response(self.object_decorator(serializer.data), status=HTTP_200_OK)
        return render(request, 'partner.html', context={'partners': serializer.data})

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        return render(request, 'partner.html', context={'partners': serializer.data})

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return render(request, 'partner.html', context={'partners': serializer.data})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        serializer = self.serializer_class(instance, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
        return render(request, 'partner.html', context={'partners': serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=HTTP_204_NO_CONTENT)
