from django.contrib import admin
from .models import Redcup, Comment, Photo

# Register your models here
admin.site.register(Redcup)
admin.site.register(Comment)
admin.site.register(Photo)
