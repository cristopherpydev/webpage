from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from articles import models
from .models import Person
from django.contrib import messages

def show_form(request):
    return render(request, 'documents/form.html', {})

def show_success(request):
    return render(request, 'documents/form_success.html', {})

def show_form(request):
    if request.method  == 'POST':
        try:
            person = Person.objects.create(
                name=request.POST.get('name'),
                mail=request.POST.get('mail'),
                phone=request.POST.get('phone'),
                experience=request.POST.get('experience'),
                dnd=bool(request.POST.get('dnd')),
                pathfinder=bool(request.POST.get('pathfinder')),
                cthulhu=bool(request.POST.get('cthulhu')),
                indie=bool(request.POST.get('indie')),
                others=bool(request.POST.get('others')),
                none=bool(request.POST.get('none')),

                interests=request.POST.get('interests'),
                modality=request.POST.get('modality'),

                first_term=bool(request.POST.get('first_term')),
                second_term=bool(request.POST.get('second_term')),
            )
            return redirect("./success/")    
        
        except IntegrityError:
            messages.error(request, "You are already signed in!")
            return redirect('/heroes/')

    return render(request, 'documents/form.html')
