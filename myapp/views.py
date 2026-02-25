from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myapp/index.html')

def doctor_single(request):
    return render(request, 'myapp/doctors_single.html')

def hospital_single(request):
    return render(request, 'myapp/hospital_single.html')