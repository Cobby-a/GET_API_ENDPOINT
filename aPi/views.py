from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

@api_view(["GET"])
def index(request):
    data = {
        "slackUsername":"boatengcobbina",
        "backend": True,
        "age": 20,
        "bio": "An junior developer who is more into fullstack development and loves python"
    }
    return JsonResponse(data)
    # return Response(data)