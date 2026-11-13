from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Student
from .serializers import StudentSerializer

@api_view(["GET", "POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def student_list(request):
    if request.method == "GET":
        return Response(StudentSerializer(Student.objects.all(), many=True).data)
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(); return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "GET": return Response(StudentSerializer(student).data)
    if request.method in ["PUT", "PATCH"]:
        serializer = StudentSerializer(student, data=request.data, partial=request.method == "PATCH")
        if serializer.is_valid():
            serializer.save(); return Response(serializer.data)
        return Response(serializer.errors, status=400)
    student.delete(); return Response(status=204)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
