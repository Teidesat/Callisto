from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AddProjectsForm, EditProjectsForm
from .models import Department, Projects

# Create your views here.


@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(
        request,
        'departments/department_list.html',
        dict(departments=departments),
    )


@login_required
def department_detail(request, department_code: str):
    department = Department.objects.get(code=department_code)
    projects = Projects.objects.filter(department=department)
    return render(
        request,
        'departments/department_detail.html',
        {'department': department, 'projects': projects},
    )


@login_required
def department_projects(request, department_code: str):
    department = Department.objects.get(code=department_code)
    return render(
        request,
        'departments/department_projects.html',
        dict(department=department),
    )


@login_required
def project_detail(request, department_code: str, project_pk: int):
    department = Department.objects.get(code=department_code)
    project = Projects.objects.get(pk=project_pk)
    return render(
        request,
        'departments/projects/project_detail.html',
        dict(project=project, department=department),
    )


@login_required
def add_project(request, department_code: str):
    department = Department.objects.get(code=department_code)
    if request.method == 'GET':
        form = AddProjectsForm()
    else:
        form = AddProjectsForm(data=request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.department = department
            project.save()
            messages.success(request, 'Projects was successfully added.')
            return redirect('departments:department-detail', department_code)
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    return render(
        request, 'departments/projects/add_project.html', {'form': form, 'department': department}
    )


@login_required
def edit_project(request, department_code: str, project_pk: int):
    department = Department.objects.get(code=department_code)
    project = Projects.objects.get(pk=project_pk)
    if request.method == 'GET':
        form = EditProjectsForm(instance=project)
    else:
        if (form := EditProjectsForm(request.POST, instance=project)).is_valid():
            project = form.save(commit=False)
            project.department = department
            project.save()
            messages.success(request, 'Changes were successfully saved.')
            return render(
                request,
                'departments/projects/edit_project.html',
                dict(project=project, department=department, form=form),
            )
    return render(
        request,
        'departments/projects/edit_project.html',
        dict(project=project, department=department, form=form),
    )


@login_required
def delete_project(request, department_code: str, project_pk: int):
    department = Department.objects.get(code=department_code)
    project = Projects.objects.get(pk=project_pk)
    project.department = department
    project.delete()
    messages.success(request, 'Projects was successfully deleted.')
    return redirect(
        'departments:department-detail',
        department.code,
    )
