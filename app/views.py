from django.shortcuts import render
from app.forms import *
from django.http.response import JsonResponse


def getPrefecture(request):

    prefecture = request.POST.get('prefecture')
    prefecutres = return_cities_by_prefecture(prefecture)
    return JsonResponse({'prefecutres': prefecutres})


def processForm(request):

    context = {}
    if request.method == 'GET':
           form  = AddressForm()
           context['form'] = form
           return render(request, 'address.html', context)

    if request.method == 'POST':
        form  = AddressForm(request.POST)
        if form.is_valid():
            selected_province = request.POST['city']
            obj = form.save(commit=False)
            obj.state = selected_province
            obj.save()