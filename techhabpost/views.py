from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to TechHubPost! This is your gateway to the world of tech knowledge."
    })