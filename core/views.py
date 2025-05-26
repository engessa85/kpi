from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import ProjectForm
from .forms import ProjectFormModel
from django.shortcuts import get_object_or_404

# Create your views here.

def landing_view(request):
    return render(request, 'landing.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin-view')
            else:
                return redirect('employee-view')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

@login_required
def admin_view(request):
    projects = ProjectForm.objects.all().order_by("-id")
    num_circles = [i for i in range(len(projects))]
    return render(request, 'admin.html', {"num_circles": num_circles})



def get_progress(request):
    progress_data = []
    projects = ProjectForm.objects.all().order_by("-id")
    for project in projects:
        progress_data.append({"id":project.id, "progress":project.progress, "project_name":project.project_name, "project_user_name":project.user.username})
    
    return JsonResponse(progress_data, safe=False)


def get_progress_employee(request):
    progress_data = []
    projects = ProjectForm.objects.filter(user = request.user).order_by("-id")
    for project in projects:
        progress_data.append({"id":project.id, "progress":project.progress, "project_name":project.project_name, "project_user_name":project.user.username})
    
    return JsonResponse(progress_data, safe=False)





@login_required
def employee_view(request):
    if request.method == "POST":
        form_data = request.session.get("form_data", {})

        form_data.update(request.POST.dict())
        request.session["form_data"] = form_data

        if "final_submit" in request.POST:
            form = ProjectFormModel(form_data)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user  
                project.save()
                del request.session["form_data"]  
                return redirect("employee-projects")

    return render(request, "employee.html")



def employee_projects_view(request):
    user = request.user
    projects = ProjectForm.objects.filter(user = user).order_by("-id")
    num_circles = [i for i in range(len(projects))]
    return render(request, 'employeeProjects.html', {"num_circles": num_circles})






@login_required
def modify_employee_projects_view(request, id):
    project = get_object_or_404(ProjectForm, id=id)

    if request.method == 'POST':
        project.project_name = request.POST.get('project_name')
        project.it_project_manager = request.POST.get('it_project_manager')
        project.it_service_owner_manager = request.POST.get('it_service_owner_manager')
        project.business_sponsor = request.POST.get('business_sponsor')
        project.business_owner = request.POST.get('business_owner')

        project.project_start_date = request.POST.get('project_start_date')
        project.portfolio_operations = request.POST.get('portfolio_operations')
        project.critical_project = bool(request.POST.get('critical_project'))  # Checkbox
        project.budget_owner = request.POST.get('budget_owner')
        project.project_budget = request.POST.get('project_budget')
        project.it_pmo = request.POST.get('it_pmo')
        project.project_finish_date = request.POST.get('project_finish_date')
        project.project_description = request.POST.get('project_description')
        project.business_value = request.POST.get('business_value')
        project.roi = request.POST.get('roi')
        project.project_scope = request.POST.get('project_scope')
        project.constraints = request.POST.get('constraints')
        project.vendor_service_support = request.POST.get('vendor_service_support')

        # Deliverables
        project.dev_first_name = request.POST.get('dev_first_name')
        project.dev_first_date = request.POST.get('dev_first_date')
        project.dev_second_name = request.POST.get('dev_second_name')
        project.dev_second_date = request.POST.get('dev_second_date')
        project.dev_third_name = request.POST.get('dev_third_name')
        project.dev_third_date = request.POST.get('dev_third_date')
        project.dev_fourth_name = request.POST.get('dev_fourth_name')
        project.dev_fourth_date = request.POST.get('dev_fourth_date')
        project.dev_fifth_name = request.POST.get('dev_fifth_name')
        project.dev_fifth_date = request.POST.get('dev_fifth_date')
        project.dev_sixth_name = request.POST.get('dev_sixth_name')
        project.dev_sixth_date = request.POST.get('dev_sixth_date')

        # Tasks
        project.first_task_name = request.POST.get('first_task_name')
        project.first_task_duration = request.POST.get('first_task_duration')
        project.first_task_starting = request.POST.get('first_task_starting')
        project.first_task_ending = request.POST.get('first_task_ending')
        project.second_task_name = request.POST.get('second_task_name')
        project.second_task_duration = request.POST.get('second_task_duration')
        project.second_task_starting = request.POST.get('second_task_starting')
        project.second_task_ending = request.POST.get('second_task_ending')
        project.third_task_name = request.POST.get('third_task_name')
        project.third_task_duration = request.POST.get('third_task_duration')
        project.third_task_starting = request.POST.get('third_task_starting')
        project.third_task_ending = request.POST.get('third_task_ending')

        # Risk
        project.first_risk_name = request.POST.get("first_risk_name")
        project.first_risk_summary = request.POST.get("first_risk_summary")
        project.first_risk_date = request.POST.get("first_risk_date")
        project.first_risk_sevirity = request.POST.get("first_risk_sevirity")
        project.first_risk_mitigation = request.POST.get("first_risk_mitigation")

        project.second_risk_name = request.POST.get("second_risk_name")
        project.second_risk_summary = request.POST.get("second_risk_summary")
        project.second_risk_date = request.POST.get("second_risk_date")
        project.second_risk_sevirity = request.POST.get("second_risk_sevirity")
        project.second_risk_mitigation = request.POST.get("second_risk_mitigation")

        project.third_risk_name = request.POST.get("third_risk_name")
        project.third_risk_summary = request.POST.get("third_risk_summary")
        project.third_risk_date = request.POST.get("third_risk_date")
        project.third_risk_sevirity = request.POST.get("third_risk_sevirity")
        project.third_risk_mitigation = request.POST.get("third_risk_mitigation")




        # stakeholder
        project.stack_first_name = request.POST.get("stack_first_name")
        project.stack_first_department = request.POST.get("stack_first_department")
        project.stack_first_role = request.POST.get("stack_first_role")

        project.stack_second_name = request.POST.get("stack_second_name")
        project.stack_second_department = request.POST.get("stack_second_department")
        project.stack_second_role = request.POST.get("stack_second_role")

        project.stack_third_name = request.POST.get("stack_third_name")
        project.stack_third_department = request.POST.get("stack_third_department")
        project.stack_third_role = request.POST.get("stack_third_role")

        project.stack_fourth_name = request.POST.get("stack_fourth_name")
        project.stack_fourth_department = request.POST.get("stack_fourth_department")
        project.stack_fourth_role = request.POST.get("stack_fourth_role")


        # Save the project
        project.save()
        return redirect('employee-projects')  # or wherever you want

    return render(request, 'employeeModify.html', {'project': project})




def logout_view(request):
    logout(request)
    return redirect("login-view")
