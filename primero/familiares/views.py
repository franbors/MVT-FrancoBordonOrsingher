from django.shortcuts import render
from django.shortcuts import render
from familiares.models import familiar

def familia(request):
    familia = familiar.objects.all()
    print(familia)
    context = {'familia': familia}
    return render(request, "template1.html", context = context) 
# Create your views here.
