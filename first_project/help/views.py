from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def help(request):
    test={'test':23}
    return render(request,"help/help.html",context=test)

