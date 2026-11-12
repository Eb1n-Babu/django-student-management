from django.urls import path
from . import views
urlpatterns = [
 path("", views.student_list, name="student-list"), path("add/", views.student_create, name="student-create"), path("<int:pk>/edit/", views.student_update, name="student-update"), path("<int:pk>/delete/", views.student_delete, name="student-delete"),
 path("cbv/", views.StudentListView.as_view(), name="student-list-cbv"), path("cbv/add/", views.StudentCreateView.as_view(), name="student-create-cbv"), path("cbv/<int:pk>/edit/", views.StudentUpdateView.as_view(), name="student-update-cbv"), path("cbv/<int:pk>/delete/", views.StudentDeleteView.as_view(), name="student-delete-cbv"),
]
