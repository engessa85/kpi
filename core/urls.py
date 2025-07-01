
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name="landing-view"),
    path('login/', views.login_view, name="login-view"),
    path('main-admin-page/', views.main_admin_view, name="main-admin-view"),

    # path('admin-page/', views.admin_view, name="admin-view"),
    path('departments/<int:dep_id>/', views.department_view, name="department-details-view"),

    path('employee-page/', views.employee_view, name="employee-view"),

    path("get-progress/<int:dep_id>/", views.get_progress, name="get-progress"),
    path("get-progress-employee/", views.get_progress_employee, name="get-progress-employee"),

    path("logout", views.logout_view, name="logout_view"),
    path("employee-projects", views.employee_projects_view, name="employee-projects"),

    path("modify-employee-project/<str:id>", views.modify_employee_projects_view, name="modify-employee-project"),
    path("admin-modify-employee-project/<str:id>", views.admin_modify_employee_projects_view, name="admin_modify_employee_projects_view"),
]
    

    