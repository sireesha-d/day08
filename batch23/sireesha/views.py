from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("<h2 style='color:white;background-color:green'>welcome to home page</h2>")
def chk(request):
	return HttpResponse("<script>alert('Hi good Afternoon')</script><h2>welcome</h2>")
def homepage(request):
	return render(request,'ht/homepage.html')
def lgn(re):
	return render(re,'ht/login.html')
def reg(rt):
	return render(rt,'ht/register.html')