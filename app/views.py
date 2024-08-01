from django.shortcuts import HttpResponse , render
from .models import Blog, Comment, Newsletter, Like



def home(request):
     blogs = Blog.objects.all()
     return render(request, 'index.html', {"blog":blogs})



# def home(request):
#     return render(request, 'index.html')



