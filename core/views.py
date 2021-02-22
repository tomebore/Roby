from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, "base.html",context)

def test(request):
    return HttpResponse("test page ")