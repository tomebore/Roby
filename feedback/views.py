from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .forms import FeedbackForm


def feedback_create(request):
    if request.method == 'POST':
       form = FeedbackForm(request.POST,request.FILES)

       if form.is_valid():
           form.instance.user = request.user
           form.save()
           return render(request , 'feedback_succsess.html')

    else:
        form = FeedbackForm()

    return render(request,'feedback.html',{'form':form}) 