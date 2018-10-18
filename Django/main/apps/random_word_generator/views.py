from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def generate(request, methods=['POST']):
    return redirect('/random_number_generater')
