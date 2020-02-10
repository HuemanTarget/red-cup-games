from django.urls import path
from . import views

urlpatterns = [
    path("", views.about, name="home"),
    path("home/", views.home, name="home"),
    path("redcups/", views.redcups_index, name="index"),
    path("redcups/<int:redcup_id>/", views.redcups_detail, name="detail"),
    path("redcups/create/", views.RedcupCreate.as_view(), name="redcups_create"),
    path("accounts/signup/", views.signup, name="signup"),
    path(
        "redcups/<int:pk>/update/", views.RedcupUpdate.as_view(), name="redcup_update"
    ),
    path(
        "redcups/<int:pk>/delete/", views.RedcupDelete.as_view(), name="redcup_delete"
    ),
    path("redcups/<int:redcup_id>/add_comment/", views.add_comment, name="add_comment"),
    path(
        "redcups/<int:pk>/commentupdate/",
        views.CommentUpdate.as_view(),
        name="comment_update",
    ),
    path(
        "redcups/<int:pk>/commentdelete/",
        views.CommentDelete.as_view(),
        name="comment_delete",
    ),
    path(
        "redcups/<int:pk>/photodelete/",
        views.PhotoDelete.as_view(),
        name="photo_delete",
    ),
    path("redcups/<int:redcup_id>/add_photo/", views.add_photo, name="add_photo"),
    path("chat/<str:room_name>/", views.room, name="room"),
    path("game/", views.game, name="game"),
]
