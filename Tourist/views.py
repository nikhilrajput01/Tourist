from django.shortcuts import render,HttpResponseRedirect
from .forms import UserData
from form.models import FormModel


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request,'about.html')


def packages(request):
    return render(request,'packages.html')


def services(request):
    return render(request,'services.html')

def booking(request):
    return render(request,'booking.html')




def contact(request):
    if request.method == 'POST':
        fd = UserData(request.POST)
        if fd.is_valid():
            nm = fd.cleaned_data['name']
            em = fd.cleaned_data['email']
            p = fd.cleaned_data['phone']
            ps = fd.cleaned_data['password']
            fm = FormModel(name=nm, email=em, num=p,password=ps)
            fm.save()
            fd = UserData()
    else:
        fd = UserData()
    data = FormModel.objects.all()
    return render(request, 'contact.html', {'fm':fd, 'data':data})


def delete(request, id):
    d = FormModel.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('contact/')


def update(request,id):
    if request.method == 'POST':
        fd = UserData(request.POST)
        if fd.is_valid():
            nm = fd.cleaned_data['name']
            em = fd.cleaned_data['email']
            p = fd.cleaned_data['phone']
            ps = fd.cleaned_data['password']
            fm = FormModel(id=id, name=nm, email=em, num=p,password=ps)
            fm.save()
            fd = UserData()
    else:
        fd = UserData()
    data = FormModel.objects.all()
    return render(request, 'update.html', {'fm':fd, 'data':data})