from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api_views import StudentViewSet, student_detail, student_list

router = DefaultRouter()

router.register("students", StudentViewSet, basename="student")
urlpatterns = \
    [path('api/token/', TokenObtainPairView.as_view()),
     path('api/token/refresh/', TokenRefreshView.as_view()),
     path("fbv/students/", student_list, name="api-student-list"),
     path("fbv/students/<int:pk>/", student_detail, name="api-student-detail"),
     path("viewset/", include(router.urls))]
