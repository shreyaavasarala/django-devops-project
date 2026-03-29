from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def docker_page(request):
    return render(request, 'docker.html')

def cicd_page(request):
    return render(request, 'cicd.html')

def architecture_page(request):
    return render(request, 'architecture.html')

def about_page(request):
    return render(request, 'about.html')