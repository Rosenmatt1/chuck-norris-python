from django.http import HttpResponse
# from django.shortcuts import render
# from .models import Product

# def index(request):
#   Product.objects.all()
#   return render(request, 'index.html', {'products': products})


def index(request):
  return HttpResponse('Hello Chuck')
