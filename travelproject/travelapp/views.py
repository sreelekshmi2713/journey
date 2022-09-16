from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Sky


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Sky.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})


# def add(request):
#     num1 = int(request.GET['t1'])
#     num2 = int(request.GET['t2'])
#     addition = num1 + num2
#     sub = num1 - num2
#     div = num1 / num2
#     mul = num1 * num2
#     return render(request, 'result.html', {'add': addition, 'sub': sub, 'div': div, 'mul': mul})
def register(request):
    if request.method=='POST':
        username=request.POST['']
        first_name = request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        user=User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)

        user.save();
        print("user created")
    return render(request, "register.html")
