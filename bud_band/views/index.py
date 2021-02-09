from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the bud band index.")
