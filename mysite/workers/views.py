from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import JobPosition, Employee
from .forms import EmployeeForm


def emp_list(request):
    template = loader.get_template('workers/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def emp_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form" = form,
    }
    return render(request, 'emp_form.html', context)

def emp_details(request, id=None):
    # instance = Post.objects.get(id=0)
    instance = get_object_or_404(Employee, id=id)
    context = {
        "first_name": instance.first_name,
        "instance": instance,
        }
    return render(request, 'emp_detail.html', context)
