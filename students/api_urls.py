from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api_views import StudentViewSet, student_detail, student_list
router = DefaultRouter()
router.register("students", StudentViewSet, basename="student")
urlpatterns = [path("fbv/students/", student_list, name="api-student-list"), path("fbv/students/<int:pk>/", student_detail, name="api-student-detail"), path("viewset/", include(router.urls))]
