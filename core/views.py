from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import ProjectForm
from .forms import ProjectFormModel

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
    projects = ProjectForm.objects.all()
    num_circles = [i for i in range(len(projects))]
    return render(request, 'admin.html', {"num_circles": num_circles})



def get_progress(request):
    progress_data = []
    projects = ProjectForm.objects.all()
    for project in projects:
        progress_data.append({"id":project.id, "progress":project.progress, "project_name":project.project_name, "project_user_name":project.user.username})
    
    return JsonResponse(progress_data, safe=False)



# @login_required
# def employee_view(request):
#     if request.method == "POST":
#         form = ProjectFormModel(request.POST)
#         print(form)
#         if form.is_valid():
#             test = form.cleaned_data["dev-first-name"]
#             print("test: ", test)
#             project = form.save(commit=False)
#             project.user = request.user  # Assign the logged-in user
#             project.save()
#     return render(request, "employee.html")



@login_required
def employee_view(request):
    if request.method == "POST":
        form_data = request.session.get("form_data", {})

        form_data.update(request.POST.dict())
        request.session["form_data"] = form_data

        if "final_submit" in request.POST:
            form = ProjectFormModel(form_data)
            if form.is_valid():
                test = form.cleaned_data["dev_first_name"]
                print(test)
                project = form.save(commit=False)
                project.user = request.user  # Assign user
                project.save()
                del request.session["form_data"]  # Clear session data
                return redirect("success_view")  # Redirect after saving

    return render(request, "employee.html")



def success_view(request):
    return render(request, "success.html")












def logout_view(request):
    logout(request)
    return redirect("login-view")
