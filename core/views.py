from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import ProjectForm, Department, UserDepartment
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
                # return redirect('admin-view')
                return redirect('main-admin-view')
            else:
                return redirect('employee-view')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

# @login_required
# def admin_view(request):
#     projects = ProjectForm.objects.all().order_by("-id")
#     num_circles = [i for i in range(len(projects))]
#     return render(request, 'admin.html', {"num_circles": num_circles})



@login_required
def department_view(request, dep_id):
    department = get_object_or_404(Department, id=dep_id)
    
    
    # Get all users in this department
    user_ids = UserDepartment.objects.filter(department=department).values_list('user_id', flat=True)
    
 
    
    # Get all projects for those users
    projects = ProjectForm.objects.filter(user_id__in=user_ids).order_by("-id")

    for project in projects:
        print(project.user.username)
        print(project.project_name)

    num_circles = [i for i in range(len(projects))]
    return render(request, 'admin.html', {"num_circles": num_circles, "dep_id":dep_id})

@login_required
def  main_admin_view(request):
    deps = Department.objects.all()
    for dep in deps:
        print(dep.average_completion())
    context = {"deps":deps}
    return render(request, "main-admin.html", context )













@login_required
def employee_view(request):
    if request.method == "POST":
        form_data = request.session.get("form_data", {})
        form_data.update(request.POST.dict())
        request.session["form_data"] = form_data

        if "final_submit" in request.POST:
            start_date_str = form_data.get("project_start_date")
            finish_date_str = form_data.get("project_finish_date")

            if finish_date_str < start_date_str:
                messages.error(request, "Project finish date must be after the start date.")
                return render(request, "employee.html", context={
                    'extra_tasks_range': range(1, 23),
                    'extra_risks_range': range(1, 4),
                    'extra_stack_range': range(1, 6),
                })

            form = ProjectFormModel(form_data, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user

                # Save uploaded signature files
                project.it_project_sig = request.FILES.get("it_project_manager_sig")
                project.it_service_sig = request.FILES.get("it_service_owner_manager_sig")
                project.it_business_sig = request.FILES.get("it_business_partener_sig")
                project.it_pmo_sig = request.FILES.get("it_pmo_manager_sig")

                # Save names
                project.it_project_name = request.POST.get("it_project_manager")
                project.it_service_name = request.POST.get("it_service_owner_manager")
                project.it_business_name = request.POST.get("it_business_partener")
                project.it_pmo_name = request.POST.get("it_pmo_manager")

                # Optional: If you also want to save Business Owner/Rep/PM
                project.business_name = request.POST.get("business_name")
                project.business_sig = request.FILES.get("business_sig")
                
                # Project Closure - Approvals
                project.cl_business_name = request.POST.get("cl_business_name")
                project.cl_business_sponser = request.POST.get("cl_business_sponser")
                project.cl_it_project_manager = request.POST.get("cl_it_project_manager")
                project.cl_it_service_owner_manager = request.POST.get("cl_it_service_owner_manager")
                project.cl_it_business_partener = request.POST.get("cl_it_business_partener")
                project.cl_it_technical_mgr = request.POST.get("cl_it_technical_mgr")
                project.cl_it_pmo_manager = request.POST.get("cl_it_pmo_manager")
                
                project.cl_business_name_sign = request.FILES.get("cl_business_name_sign")
                project.cl_business_sponser_sign = request.FILES.get("cl_business_sponser_sign")
                project.cl_it_project_manager_sig = request.FILES.get("cl_it_project_manager_sig")
                project.cl_it_service_owner_manager_sig = request.FILES.get("cl_it_service_owner_manager_sig")
                project.cl_it_business_partener_sig = request.FILES.get("cl_it_business_partener_sig")
                project.cl_it_technical_mgr_sign = request.FILES.get("cl_it_technical_mgr_sign")
                project.cl_it_pmo_manager_sig = request.FILES.get("cl_it_pmo_manager_sig")
                

                project.full_clean()
                project.save()
                del request.session["form_data"]
                return redirect("employee-projects")

    return render(request, "employee.html", context={
        'extra_tasks_range': range(1, 23),
        'extra_risks_range': range(1, 4),
        'extra_stack_range': range(1, 6),
    })



#########################


def get_progress(request, dep_id):
    department = get_object_or_404(Department, id=dep_id)
    # Get all users in this department
    user_ids = UserDepartment.objects.filter(department=department).values_list('user_id', flat=True)

    # Get all projects for those users
    projects = ProjectForm.objects.filter(user_id__in=user_ids).order_by("-id")

    progress_data = []
    for project in projects:
        progress_data.append({"id":project.id, "progress":project.progress, "project_name":project.project_name, "project_user_name":project.user.username})
    
    return JsonResponse(progress_data, safe=False)



def get_progress_employee(request):
    progress_data = []
    projects = ProjectForm.objects.filter(user = request.user).order_by("-id")
    for project in projects:
        progress_data.append({"id":project.id, "progress":project.progress, "project_name":project.project_name, "project_user_name":project.user.username})
    
    return JsonResponse(progress_data, safe=False)




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
        project.it_project_manager_field = request.POST.get('it_project_manager_field')
        project.it_service_owner_manager_field = request.POST.get('it_service_owner_manager_field')
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

        if project.project_start_date and project.project_finish_date and project.project_start_date > project.project_finish_date:
            messages.error(request, "Finish date must be after the start date.")
            return render(request, 'employeeModify.html', {'project': project})


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

        project.dev_extra_name_1 = request.POST.get('dev_extra_name_1')
        project.dev_extra_date_1 = request.POST.get('dev_extra_date_1')

        project.dev_extra_name_2 = request.POST.get('dev_extra_name_2')
        project.dev_extra_date_2 = request.POST.get('dev_extra_date_2')

        project.dev_extra_name_3 = request.POST.get('dev_extra_name_3')
        project.dev_extra_date_3 = request.POST.get('dev_extra_date_3')

        project.dev_extra_name_4 = request.POST.get('dev_extra_name_4')
        project.dev_extra_date_4 = request.POST.get('dev_extra_date_4')

        project.dev_extra_name_5 = request.POST.get('dev_extra_name_5')
        project.dev_extra_date_5 = request.POST.get('dev_extra_date_5')

        project.dev_extra_name_6 = request.POST.get('dev_extra_name_6')
        project.dev_extra_date_6 = request.POST.get('dev_extra_date_6')

        project.dev_extra_name_7 = request.POST.get('dev_extra_name_7')
        project.dev_extra_date_7 = request.POST.get('dev_extra_date_7')

        project.dev_extra_name_8 = request.POST.get('dev_extra_name_8')
        project.dev_extra_date_8 = request.POST.get('dev_extra_date_8')

        project.dev_extra_name_9 = request.POST.get('dev_extra_name_9')
        project.dev_extra_date_9 = request.POST.get('dev_extra_date_9')

        project.dev_extra_name_10 = request.POST.get('dev_extra_name_10')
        project.dev_extra_date_10 = request.POST.get('dev_extra_date_10')

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


        project.task_name_extra_1 = request.POST.get('task_name_extra_1')
        project.task_duration_extra_1 = request.POST.get('task_duration_extra_1')
        project.task_starting_extra_1 = request.POST.get('task_starting_extra_1')
        project.task_ending_extra_1 = request.POST.get('task_ending_extra_1')

        project.task_name_extra_2 = request.POST.get('task_name_extra_2')
        project.task_duration_extra_2 = request.POST.get('task_duration_extra_2')
        project.task_starting_extra_2 = request.POST.get('task_starting_extra_2')
        project.task_ending_extra_2 = request.POST.get('task_ending_extra_2')

        project.task_name_extra_3 = request.POST.get('task_name_extra_3')
        project.task_duration_extra_3 = request.POST.get('task_duration_extra_3')
        project.task_starting_extra_3 = request.POST.get('task_starting_extra_3')
        project.task_ending_extra_3 = request.POST.get('task_ending_extra_3')

        project.task_name_extra_4 = request.POST.get('task_name_extra_4')
        project.task_duration_extra_4 = request.POST.get('task_duration_extra_4')
        project.task_starting_extra_4 = request.POST.get('task_starting_extra_4')
        project.task_ending_extra_4 = request.POST.get('task_ending_extra_4')

        project.task_name_extra_5 = request.POST.get('task_name_extra_5')
        project.task_duration_extra_5 = request.POST.get('task_duration_extra_5')
        project.task_starting_extra_5 = request.POST.get('task_starting_extra_5')
        project.task_ending_extra_5 = request.POST.get('task_ending_extra_5')

        project.task_name_extra_6 = request.POST.get('task_name_extra_6')
        project.task_duration_extra_6 = request.POST.get('task_duration_extra_6')
        project.task_starting_extra_6 = request.POST.get('task_starting_extra_6')
        project.task_ending_extra_6 = request.POST.get('task_ending_extra_6')

        project.task_name_extra_7 = request.POST.get('task_name_extra_7')
        project.task_duration_extra_7 = request.POST.get('task_duration_extra_7')
        project.task_starting_extra_7 = request.POST.get('task_starting_extra_7')
        project.task_ending_extra_7 = request.POST.get('task_ending_extra_7')

        project.task_name_extra_8 = request.POST.get('task_name_extra_8')
        project.task_duration_extra_8 = request.POST.get('task_duration_extra_8')
        project.task_starting_extra_8 = request.POST.get('task_starting_extra_8')
        project.task_ending_extra_8 = request.POST.get('task_ending_extra_8')

        project.task_name_extra_9 = request.POST.get('task_name_extra_9')
        project.task_duration_extra_9 = request.POST.get('task_duration_extra_9')
        project.task_starting_extra_9 = request.POST.get('task_starting_extra_9')
        project.task_ending_extra_9 = request.POST.get('task_ending_extra_9')

        project.task_name_extra_10 = request.POST.get('task_name_extra_10')
        project.task_duration_extra_10 = request.POST.get('task_duration_extra_10')
        project.task_starting_extra_10 = request.POST.get('task_starting_extra_10')
        project.task_ending_extra_10 = request.POST.get('task_ending_extra_10')

        project.task_name_extra_11 = request.POST.get('task_name_extra_11')
        project.task_duration_extra_11 = request.POST.get('task_duration_extra_11')
        project.task_starting_extra_11 = request.POST.get('task_starting_extra_11')
        project.task_ending_extra_11 = request.POST.get('task_ending_extra_11')

        project.task_name_extra_12 = request.POST.get('task_name_extra_12')
        project.task_duration_extra_12 = request.POST.get('task_duration_extra_12')
        project.task_starting_extra_12 = request.POST.get('task_starting_extra_12')
        project.task_ending_extra_12 = request.POST.get('task_ending_extra_12')

        project.task_name_extra_13 = request.POST.get('task_name_extra_13')
        project.task_duration_extra_13 = request.POST.get('task_duration_extra_13')
        project.task_starting_extra_13 = request.POST.get('task_starting_extra_13')
        project.task_ending_extra_13 = request.POST.get('task_ending_extra_13')

        project.task_name_extra_14 = request.POST.get('task_name_extra_14')
        project.task_duration_extra_14 = request.POST.get('task_duration_extra_14')
        project.task_starting_extra_14 = request.POST.get('task_starting_extra_14')
        project.task_ending_extra_14 = request.POST.get('task_ending_extra_14')

        project.task_name_extra_15 = request.POST.get('task_name_extra_15')
        project.task_duration_extra_15 = request.POST.get('task_duration_extra_15')
        project.task_starting_extra_15 = request.POST.get('task_starting_extra_15')
        project.task_ending_extra_15 = request.POST.get('task_ending_extra_15')

        project.task_name_extra_16 = request.POST.get('task_name_extra_16')
        project.task_duration_extra_16 = request.POST.get('task_duration_extra_16')
        project.task_starting_extra_16 = request.POST.get('task_starting_extra_16')
        project.task_ending_extra_16 = request.POST.get('task_ending_extra_16')

        project.task_name_extra_17 = request.POST.get('task_name_extra_17')
        project.task_duration_extra_17 = request.POST.get('task_duration_extra_17')
        project.task_starting_extra_17 = request.POST.get('task_starting_extra_17')
        project.task_ending_extra_17 = request.POST.get('task_ending_extra_17')

        project.task_name_extra_18 = request.POST.get('task_name_extra_18')
        project.task_duration_extra_18 = request.POST.get('task_duration_extra_18')
        project.task_starting_extra_18 = request.POST.get('task_starting_extra_18')
        project.task_ending_extra_18 = request.POST.get('task_ending_extra_18')

        project.task_name_extra_19 = request.POST.get('task_name_extra_19')
        project.task_duration_extra_19 = request.POST.get('task_duration_extra_19')
        project.task_starting_extra_19 = request.POST.get('task_starting_extra_19')
        project.task_ending_extra_19 = request.POST.get('task_ending_extra_19')

        project.task_name_extra_20 = request.POST.get('task_name_extra_20')
        project.task_duration_extra_20 = request.POST.get('task_duration_extra_20')
        project.task_starting_extra_20 = request.POST.get('task_starting_extra_20')
        project.task_ending_extra_20 = request.POST.get('task_ending_extra_20')

        project.task_name_extra_21 = request.POST.get('task_name_extra_21')
        project.task_duration_extra_21 = request.POST.get('task_duration_extra_21')
        project.task_starting_extra_21 = request.POST.get('task_starting_extra_21')
        project.task_ending_extra_21 = request.POST.get('task_ending_extra_21')

        project.task_name_extra_22 = request.POST.get('task_name_extra_22')
        project.task_duration_extra_22 = request.POST.get('task_duration_extra_22')
        project.task_starting_extra_22 = request.POST.get('task_starting_extra_22')
        project.task_ending_extra_22 = request.POST.get('task_ending_extra_22')


        

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


        project.risk_name_1 = request.POST.get("risk_name_1")
        project.risk_summary_1 = request.POST.get("risk_summary_1")
        project.risk_date_1 = request.POST.get("risk_date_1")
        project.risk_sevirity_1 = request.POST.get("risk_sevirity_1")
        project.risk_mitigation_1 = request.POST.get("risk_mitigation_1")

        project.risk_name_2 = request.POST.get("risk_name_2")
        project.risk_summary_2 = request.POST.get("risk_summary_2")
        project.risk_date_2 = request.POST.get("risk_date_2")
        project.risk_sevirity_2 = request.POST.get("risk_sevirity_2")
        project.risk_mitigation_2 = request.POST.get("risk_mitigation_2")

        project.risk_name_3 = request.POST.get("risk_name_3")
        project.risk_summary_3 = request.POST.get("risk_summary_3")
        project.risk_date_3 = request.POST.get("risk_date_3")
        project.risk_sevirity_3 = request.POST.get("risk_sevirity_3")
        project.risk_mitigation_3 = request.POST.get("risk_mitigation_3")




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


        project.stack_name_extra_1 = request.POST.get("stack_name_extra_1")
        project.stack_department_extra_1 = request.POST.get("stack_department_extra_1")
        project.stack_role_extra_1 = request.POST.get("stack_role_extra_1")

        project.stack_name_extra_2 = request.POST.get("stack_name_extra_2")
        project.stack_department_extra_2 = request.POST.get("stack_department_extra_2")
        project.stack_role_extra_2 = request.POST.get("stack_role_extra_2")

        project.stack_name_extra_3 = request.POST.get("stack_name_extra_3")
        project.stack_department_extra_3 = request.POST.get("stack_department_extra_3")
        project.stack_role_extra_3 = request.POST.get("stack_role_extra_3")

        project.stack_name_extra_4 = request.POST.get("stack_name_extra_4")
        project.stack_department_extra_4 = request.POST.get("stack_department_extra_4")
        project.stack_role_extra_4 = request.POST.get("stack_role_extra_4")

        project.stack_name_extra_5 = request.POST.get("stack_name_extra_5")
        project.stack_department_extra_5 = request.POST.get("stack_department_extra_5")
        project.stack_role_extra_5 = request.POST.get("stack_role_extra_5")

        # Governance
        project.c_plan = request.POST.get("c_plan")
        project.ms_project = request.POST.get("ms_project")
        project.project_report = request.POST.get("project_report")


        # Sig fields
        project.business_name = request.POST.get("business_name")
        project.it_project_manager = request.POST.get("it_project_manager")
        project.it_service_owner_manager = request.POST.get("it_service_owner_manager")
        project.it_business_partener = request.POST.get("it_business_partener")
        project.it_pmo_manager = request.POST.get("it_pmo_manager")

        # Update signature files only if new ones are uploaded
        if request.FILES.get("business_sig"):
            project.business_sig = request.FILES["business_sig"]
        if request.FILES.get("it_project_manager_sig"):
            project.it_project_manager_sig = request.FILES["it_project_manager_sig"]
        if request.FILES.get("it_service_owner_manager_sig"):
            project.it_service_owner_manager_sig = request.FILES["it_service_owner_manager_sig"]
        if request.FILES.get("it_business_partener_sig"):
            project.it_business_partener_sig = request.FILES["it_business_partener_sig"]
        if request.FILES.get("it_pmo_manager_sig"):
            project.it_pmo_manager_sig = request.FILES["it_pmo_manager_sig"]
        
        # Project Closure - General Information 
        project.cl_project_name = request.POST.get("cl_project_name")
        project.cl_actual_start_date = request.POST.get("cl_actual_start_date")
        
        project.cl_project_manager = request.POST.get("cl_project_manager")
        project.cl_actual_finish_date = request.POST.get("cl_actual_finish_date")
        
        project.cl_reason_status = request.POST.get("cl_reason_status")
        project.cl_reason_status_reason = request.POST.get("cl_reason_status_reason")
        
        # Project Closure - Actual Deliverables
        
        project.cl_actual_d_1 = request.POST.get("cl_actual_d_1")
        project.cl_actual_d_2 = request.POST.get("cl_actual_d_2")
        project.cl_actual_d_3 = request.POST.get("cl_actual_d_3")
        project.cl_actual_d_4 = request.POST.get("cl_actual_d_4")
        project.cl_actual_d_5 = request.POST.get("cl_actual_d_5")
        project.cl_actual_d_6 = request.POST.get("cl_actual_d_6")
        project.cl_actual_d_7 = request.POST.get("cl_actual_d_7")
        project.cl_actual_d_8 = request.POST.get("cl_actual_d_8")
        project.cl_actual_d_9 = request.POST.get("cl_actual_d_9")
        project.cl_actual_d_10 = request.POST.get("cl_actual_d_10")
        
        # Project Closure - cls
        
        
        project.cl_cr_name1 = request.POST.get("cl_cr_name1")
        project.cl_cost1 = request.POST.get("cl_cost1")

        project.cl_cr_name2 = request.POST.get("cl_cr_name2")
        project.cl_cost2 = request.POST.get("cl_cost2")

        project.cl_cr_name3 = request.POST.get("cl_cr_name3")
        project.cl_cost3 = request.POST.get("cl_cost3")

        project.cl_cr_name4 = request.POST.get("cl_cr_name4")
        project.cl_cost4 = request.POST.get("cl_cost4")

        project.cl_cr_name5 = request.POST.get("cl_cr_name5")
        project.cl_cost5 = request.POST.get("cl_cost5")

        project.cl_cr_name6 = request.POST.get("cl_cr_name6")
        project.cl_cost6 = request.POST.get("cl_cost6")

        project.cl_cr_name7 = request.POST.get("cl_cr_name7")
        project.cl_cost7 = request.POST.get("cl_cost7")

        project.cl_cr_name8 = request.POST.get("cl_cr_name8")
        project.cl_cost8 = request.POST.get("cl_cost8")

        project.cl_cr_name9 = request.POST.get("cl_cr_name9")
        project.cl_cost9 = request.POST.get("cl_cost9")

        project.cl_cr_name10 = request.POST.get("cl_cr_name10")
        project.cl_cost10 = request.POST.get("cl_cost10")

        project.cl_cr_name11 = request.POST.get("cl_cr_name11")
        project.cl_cost11 = request.POST.get("cl_cost11")

        project.cl_cr_name12 = request.POST.get("cl_cr_name12")
        project.cl_cost12 = request.POST.get("cl_cost12")

        project.cl_cr_name13 = request.POST.get("cl_cr_name13")
        project.cl_cost13 = request.POST.get("cl_cost13")

        project.cl_cr_name14 = request.POST.get("cl_cr_name14")
        project.cl_cost14 = request.POST.get("cl_cost14")

        project.cl_cr_name15 = request.POST.get("cl_cr_name15")
        project.cl_cost15 = request.POST.get("cl_cost15")
        
        # Project Closure - Lessons Learned
        
        project.cl_des1 = request.POST.get("cl_des1")
        project.cl_imp1 = request.POST.get("cl_imp1")
        project.cl_ana1 = request.POST.get("cl_ana1")
        project.cl_re1 = request.POST.get("cl_re1")
        
        project.cl_des2 = request.POST.get("cl_des2")
        project.cl_imp2 = request.POST.get("cl_imp2")
        project.cl_ana2 = request.POST.get("cl_ana2")
        project.cl_re2 = request.POST.get("cl_re2")
        
        project.cl_des3 = request.POST.get("cl_des3")
        project.cl_imp3 = request.POST.get("cl_imp3")
        project.cl_ana3 = request.POST.get("cl_ana3")
        project.cl_re3 = request.POST.get("cl_re3")
        
        
        # Project Closure - Approvals
        project.cl_business_name = request.POST.get("cl_business_name")
        project.cl_business_sponser = request.POST.get("cl_business_sponser")
        project.cl_it_project_manager = request.POST.get("cl_it_project_manager")
        project.cl_it_service_owner_manager = request.POST.get("cl_it_service_owner_manager")
        project.cl_it_business_partener = request.POST.get("cl_it_business_partener")
        project.cl_it_technical_mgr = request.POST.get("cl_it_technical_mgr")
        project.cl_it_pmo_manager = request.POST.get("cl_it_pmo_manager")
        
        
        if request.FILES.get("cl_business_name_sign"):
            project.cl_business_name_sign = request.FILES.get("cl_business_name_sign")
        if request.FILES.get("cl_business_sponser_sign"):
            project.cl_business_sponser_sign = request.FILES.get("cl_business_sponser_sign")
        if request.FILES.get("cl_it_project_manager_sig"):
            project.cl_it_project_manager_sig = request.FILES.get("cl_it_project_manager_sig")
        if request.FILES.get("cl_it_service_owner_manager_sig"):
            project.cl_it_service_owner_manager_sig = request.FILES.get("cl_it_service_owner_manager_sig")
        if request.FILES.get("cl_it_business_partener_sig"):
            project.cl_it_business_partener_sig = request.FILES.get("cl_it_business_partener_sig")
        if request.FILES.get("cl_it_technical_mgr_sign"):
            project.cl_it_technical_mgr_sign = request.FILES.get("cl_it_technical_mgr_sign")
        if request.FILES.get("cl_it_pmo_manager_sig"):
            project.cl_it_pmo_manager_sig = request.FILES.get("cl_it_pmo_manager_sig")
        
        
        # Save the project
        project.full_clean()
        project.save()
        return redirect('employee-projects')  # or wherever you want
    


    return render(request, 'employeeModify.html', {'project': project})


@login_required
def admin_modify_employee_projects_view(request, id):
    project = get_object_or_404(ProjectForm, id=id)
    return render(request, 'adminemployeeModify.html', {'project': project})


def logout_view(request):
    logout(request)
    return redirect("login-view")
