from django.shortcuts import render, redirect, Http404
from .import models

# Create your views here.

def user_login(request):
    return render(request, "testapp/login.html")

def dashboard(request):
    return render(request, "testapp/dashboard.html")


def user_profile(request):
    return render(request, "testapp/user_profile.html")

def department(request, **kwargs):
    print("kwargs: ", kwargs)

    if kwargs['slug'] == "list":
        if request.method == "GET":
            get_department = models.Department.objects.all()
            return render(request, "testapp/department_list.html", {'get_department': get_department}) 
    elif kwargs['slug'] == "add":
        if request.method == "GET":
            return render(request, "testapp/department_add.html")
        elif request.method == "POST":
            models.Department.objects.create(dept_name = request.POST["dept_name"])
            return render(request, "testapp/department_add.html")
    elif kwargs['slug'] == "put":
        if request.method == "GET":
            return render(request, "testapp/department_add.html")
        elif request.method == "POST":
            models.Department.objects.create(dept_name = request.POST["dept_name"])
            return render(request, "testapp/department_add.html")
    elif kwargs['slug'] == "details" and 'id' in kwargs:
        if request.method == "GET":
            get_department = models.Department.objects.filter(id=kwargs['id'])
            print('get_department: ', get_department)
            return render(request, "testapp/department_details.html", {'get_department': get_department})         
    else:
        raise Http404 


