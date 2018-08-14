from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .models import Employee
from .forms import CreateForm
# Create your views here.

def listview(request):
    queryset = Employee.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, 'employees/list.html', context)

def createview(request):
    form = CreateForm(request.POST, request.FILES)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/employees/')
    if form.errors:
        errors = form.errors

    template_name = 'employees/forms.html'
    context = {
        'form' : form,
        'errors' : errors
    }
    return render(request, template_name, context)

def editview(request, id=None):
    instance = get_object_or_404(Employee, id=id)
    form = CreateForm(request.POST or None, request.FILES or None, instance=instance)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/employees/')
    if form.errors:
        errors = form.errors

    template_name = 'employees/form.html'
    context = {
        'form' : form,
        'errors' : errors
    }
    return render(request, template_name, context)

def deleteview(request, id=None):
    instance = get_object_or_404(Employee, id=id)
    instance.delete()
    return redirect('employees:list')