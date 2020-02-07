from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Redcup
from django.views.generic import ListView, DetailView
# Define the home view


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def redcups_index(request):
    # redcups = Redcup.objects.filter(user=request.user)
    redcups = Redcup.objects.all()
    return render(request, 'redcup/index.html', {'redcups': redcups})


class RedcupCreate( CreateView):
    model = Redcup
    fields = "__all__"
    success_url = '/redcups/'

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


def redcups_detail(request, redcup_id):
    redcup = Redcup.objects.get(id=redcup_id)
    return render(request, 'redcup/detail.html', {
        'redcup': redcup
    })

class RedcupUpdate(UpdateView):
    model = Redcup
    fields = '__all__'

class RedcupDelete(DeleteView):
    model = Redcup
    success_url = '/redcup/'
