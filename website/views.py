from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    return render(request,"index.html")
def surya(request):
    return HttpResponse("hellow world!")
def Course(request):
    return HttpResponse("hii my name suryakant patel")
def CourseDetail(request,Courseid):
    return HttpResponse(Courseid)