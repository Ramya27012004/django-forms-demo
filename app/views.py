from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def htmlforms(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        return HttpResponse(f'username is {un} and pasword is {pw}')

    return render(request,'htmlforms.html')