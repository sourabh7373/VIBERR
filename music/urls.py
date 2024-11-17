from django.urls import path, re_path
from . import views


app_name = 'music'  # This sets the namespace for the app

urlpatterns = [
    path('', views.index, name='index'),  # for home page
    path('register/', views.register, name='register'),  # registration page
    path('login_user/', views.login_user, name='login_user'),  # login page
    path('logout_user/', views.logout_user, name='logout_user'),  # logout page
    
    # Using re_path for regex capturing groups
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),  # detail page for a specific album
    re_path(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),  # mark song as favorite
    re_path(r'^songs/(?P<filter_by>[a-zA-Z]+)/$', views.songs, name='songs'),  # filter songs by a parameter
    
    # Other views with specific album or song-related actions
    path('create_album/', views.create_album, name='create_album'),  # create new album
    re_path(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),  # create song in album
    re_path(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),  # delete song from album
    re_path(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),  # favorite album
    re_path(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),  # delete album
]
