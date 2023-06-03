from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body bgcolor=blue><h1><center>welcome to ManikantaReddyIT</center></h1><body></html>""")
    return res
