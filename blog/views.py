from django.shortcuts import render
from django.http import HttpResponse

def BlogView(request):
    return HttpResponse('<h1>Welcome!<br>Blog Page</h1>')

def BlogPost(request, postid):
    return HttpResponse('<h1>Welcome!<br>Blog Post <br> post id:</h1>' + str(postid) )