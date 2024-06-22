from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='SignUp'),
    path('login/',UserLogin.as_view(),name='login'),
    path('upload/',UploadFile.as_view(),name='upload'),
    path('download-file/<int:file_id>/', DownloadFileView.as_view(), name='download-file'),
    path('allfiles/',ListFiles.as_view(),name='allfiles')
]
