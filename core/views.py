from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, "base.html",context)

def shop(request):
    context = {}
    return render(request, "shop.html",context)
def test(request):
    return HttpResponse("test page ")