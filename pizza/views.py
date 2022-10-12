from django.shortcuts import render

# Create your views here.

def startingPage(request):
    context = {
        
    }
    return render(request, "pizza/index.html", context)