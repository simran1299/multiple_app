from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':200 , 'b':300}
    return render(request,'a1_first.html',d)
def a1_second(request):
    d={'a':200 , 'b':300, 'c':400 }
    return render(request,'a1_second.html',d)
