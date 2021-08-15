from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.http import Http404
# Create your views here.
def home(request):
    employees=Employee.objects.all()
    return render(request,'home.html',{'employees':employees})

def employee_detail(request, employee_id):
    try:
        employee=Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        raise Http404('Employee does not exist')
    return render(request,'employee_detail.html',{'employee':employee})