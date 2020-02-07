from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.about, name='home'),
    path('redcups/', views.redcups_index, name='index'),
    path('redcups/<int:redcup_id>/', views.redcups_detail, name='detail'),
    path('redcups/create/', views.RedcupCreate.as_view(), name='redcups_create'),
    path('accounts/signup/', views.signup, name='signup'),
    path('redcups/<int:pk>/update/', views.RedcupUpdate.as_view(), name='redcup_update'),
    path('redcups/<int:pk>/delete/', views.RedcupDelete.as_view(), name='redcup_delete'),
]
