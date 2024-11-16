from django.shortcuts import render
from .models import AddtoPeople
#from django.http import HttpResponse
#from django.template import loader


def HomePage(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        obituary_text = request.POST['obituary_text']

        new_AddtoPeople = AddtoPeople(name=name, date_of_birth=date_of_birth, date_of_death=date_of_death, obituary_text=obituary_text)
        new_AddtoPeople.save()

        #template = loader.get_template('index.html')
        #return HttpResponse(template.render())
    return render(request, 'obituary_people/index.html', {})


