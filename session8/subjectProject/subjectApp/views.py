from re import template
from sre_constants import SUCCESS
from django.shortcuts import render
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.
class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'home.html', {'majors': majors , 'subjects':subjects })
    

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')


class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = "EditSubject.html"
    success_url = reverse_lazy('home') 

def computerSubjectView(request):
    subjects = Subject.objects.all()
    computerMajor = subjects.filter(major__name='산업정보디자인')

    return render(request, 'computer.html', {'computerMajor': computerMajor})