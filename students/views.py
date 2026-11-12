from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import StudentForm
from .models import Student

def student_list(request):
    return render(request, "students/student_list.html", {"students": Student.objects.all(), "view_type": "Function-based"})
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save(); return redirect("student-list")
    return render(request, "students/student_form.html", {"form": form, "title": "Add student"})
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save(); return redirect("student-list")
    return render(request, "students/student_form.html", {"form": form, "title": "Edit student"})
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete(); return redirect("student-list")
    return render(request, "students/student_confirm_delete.html", {"student": student})
class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"
    extra_context = {"view_type": "Class-based"}
class StudentCreateView(CreateView):
    model = Student; form_class = StudentForm; template_name = "students/student_form.html"; success_url = reverse_lazy("student-list")
    extra_context = {"title": "Add student (CBV)"}
class StudentUpdateView(UpdateView):
    model = Student; form_class = StudentForm; template_name = "students/student_form.html"; success_url = reverse_lazy("student-list")
    extra_context = {"title": "Edit student (CBV)"}
class StudentDeleteView(DeleteView):
    model = Student; template_name = "students/student_confirm_delete.html"; success_url = reverse_lazy("student-list")
