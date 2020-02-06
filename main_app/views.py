from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Redcup

# Define the home view


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
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


class RedcupCreate(LoginRequiredMixin, CreateView):
    model = Redcup
    fields = "__all__"
    success_url = '/redcup/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def redcups_detail(request, redcup_id):
    redcup = Redcup.objects.get(id=redcup_id)
    return render(request, 'redcups/detail.html', {
        'redcup': redcup
    })
