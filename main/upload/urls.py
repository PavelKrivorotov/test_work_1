from django.urls import path

from upload import views


urlpatterns = [
    path('upload/', views.UploadFileView.as_view()),
    path('list/', views.ListFileView.as_view()),
]

