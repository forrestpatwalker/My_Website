from django.shortcuts import render
from my_website.models import Project
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'my_website/index.html')


def skills(request):
    return render(request, 'my_website/skills.html')


def contact(request):
    return render(request, 'my_website/contact.html')


def about(request):
    return render(request, 'my_website/about.html')


def work(request):
    # query the database to return all projects objects
    projects = Project.objects.all()
    return render(request, 'my_website/work.html', {'projects': projects})


def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'my_website/details.html', {'project': project})
