from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    response = "Testing 123!"
    return HttpResponse(response)
