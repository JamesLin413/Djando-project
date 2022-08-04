from distutils import errors
from distutils.log import error
from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import is_valid_path
from restaurants.models import Restaurant, Food, Comment
from django.utils import timezone
from restaurants.forms import CommentForm

def menu(request):
    if 'id' in request.GET and request.GET['id'] != '':
        restaurant = Restaurant.objects.get(id = request.GET['id'])
        return render(request,'menu.html',   locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name']!='':
        return HttpResponse('Welcome!~' +  request.GET['user_name'])
    else:
        return render(request, 'welcome.html', locals())

def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants_list.html', locals())

def comment(request, id):
    if id:
        r = Restaurant.objects.get(id = id)
    else:
        return HttpResponseRedirect("/restaurant_list/")
    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            visitor = f.cleaned_data['visitor']
            content = f.cleaned_data['content']
            email = f.cleaned_data['email']
            date_time = timezone.localtime(timezone.now())
            Comment.objects.create(visitor = visitor, email = email, content = content, date_time = date_time, restaurant = r)
            visitor, content, email = ('', '', '')
            f = CommentForm(initial={'content':'我沒意見'})
    else:
        f = CommentForm(initial={'content':'我沒意見'})
    return render(request , 'comment.html', locals())