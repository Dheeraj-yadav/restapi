from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Table
from . serializers import TableSerializer


def index(request):
    return render(request, 'home.html')


class TableList(APIView):

    def get(self, request):
        Table1 = Table.objects.all()
        serializer = TableSerializer(Table1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

