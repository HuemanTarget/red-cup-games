from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Redcup, Comment, Photo
from django.views.generic import ListView, DetailView
from .forms import CommentForm


S3_BASE_URL = "https://s3-us-west-1.amazonaws.com/"
BUCKET = "redcupgames"

# Define the home view


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def redcups_index(request):
    redcups = Redcup.objects.filter(user=request.user)
    redcups = Redcup.objects.all()
    return render(request, "redcup/index.html", {"redcups": redcups})


class RedcupCreate(CreateView):
    model = Redcup
    fields = ["name", "rules", "players", "link"]
    success_url = "/redcups/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def redcups_detail(request, redcup_id):
    redcup = Redcup.objects.get(id=redcup_id)
    comment_form = CommentForm()
    return render(
        request, "redcup/detail.html", {"redcup": redcup, "comment_form": comment_form}
    )


def add_photo(request, redcup_id):
    photo_file = request.FILES.get("photo-file", None)
    if photo_file:
        s3 = boto3.client("s3")
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind(".") :]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, redcup_id=redcup_id)
            photo.save()
        except:
            print("An error occurred uploading file to S3")
    return redirect("detail", redcup_id=redcup_id)


def add_comment(request, redcup_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.redcup_id = redcup_id
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        new_comment.save()
    return redirect("detail", redcup_id=redcup_id)


# @login_required
class RedcupUpdate(UpdateView):
    model = Redcup
    fields = "__all__"


# @login_required
class RedcupDelete(DeleteView):
    model = Redcup
    success_url = "/redcups/"

    # @login_required


class CommentUpdate(UpdateView):
    model = Comment
    fields = ["comment"]
    success_url = "/redcups/{redcup_id}"


# @login_required
class CommentDelete(DeleteView):
    model = Comment
    success_url = "/redcups/{redcup_id}"
