from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def health_check_view(request: Request) -> Response:
    return HttpResponse('OK')


@api_view(['GET'])
def home_view(request: Request) -> Response:
    return render(request, 'home/index.html')
