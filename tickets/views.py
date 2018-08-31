from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Ticket
from .forms import CreateForm
# Create your views here.

@login_required
def listview(request):
    queryset = Ticket.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, 'tickets/list.html', context)

@login_required
def createview(request):
    form = CreateForm(request.POST, request.FILES)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/tickets/")
    if form.errors:
        errors = form.errors

    template_name = 'tickets/forms.html'
    context = {"form" : form, "errors" : errors}
    return render(request, template_name, context)

@login_required
def editview(request, id=None):
    instance = get_object_or_404(Ticket, id=id)
    form = CreateForm(request.POST or None, request.FILES or None, instance=instance)
    errors = None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/tickets/")
    if form.errors:
        errors = form.errors

    template_name = 'tickets/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)

@login_required
def deleteview(request, id=None):
    instance = get_object_or_404(Ticket, id=id)
    instance.delete()
    return redirect('tickets:list')

@login_required
def detailview(request, id=None):
    object = get_object_or_404(Ticket, id=id)
    return render(request, 'tickets/detail.html', {'object': object})