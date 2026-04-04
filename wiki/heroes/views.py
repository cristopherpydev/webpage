from django.shortcuts import render, redirect
from django.http import HttpResponse
from articles import models
from . import models
def show_form(request):
    return render(request, 'documents/form.html', {})

def show_success(request):
    return render(request, 'documents/form_success.html', {})

def show_form(request):
    print("ENTRANDO EN LA VISTA")

    if request.method == 'POST':
        print("POST DETECTADO")
        return redirect("./success/")

    return render(request, 'documents/form.html')
