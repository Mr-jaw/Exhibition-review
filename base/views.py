from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Reviews
from django.urls import reverse
import time

# Create your views here.

def index(request):
    return render(request, 'index.html')


def addrecord(request):
    school_got = request.POST['school']
    review_got = request.POST['review']
    school = Reviews(school=school_got, review=review_got)
    school.save()
    return HttpResponseRedirect('thankyou')

def thankyou(request):
    return render(request, 'thankyou.html')
