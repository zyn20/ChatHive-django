from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def say_HelloWorld(request):
    return HttpResponse('Hello World From say_HellowWorld')

def say_Goodbye(request):
    return HttpResponse('Good Bye ! From say_Goodbye Function')

def display_date(request):
    date_obj = datetime.today().year
    res = f'The Year is: {date_obj}'  
    return HttpResponse(res)

