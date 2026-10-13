from django.shortcuts import render,redirect

from django.http import HttpResponse
from .forms import EmployeeForm




def home(request):
    employees = [
        {'name': 'Rahul', 'department': 'IT'},
        {'name': 'Amit', 'department': 'HR'},
        {'name': 'Priya', 'department': 'Finance'},
    ]

    return render(
        request,
        'employees/home.html',
        {'employees': employees}
    )

def dashboard(request):
    context = {
        'name': 'Ajay',
        'total_employees': 3,
    }

    return render(request, 'employees/dashboard.html', context)

from django.shortcuts import render
from .models import Employee


def employee_list(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees
    }

    return render(request, 'employees/employee_list.html', context)

def add_employee(request):

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(
        request,
        'employees/add_employee.html',
        {'form': form}
    )