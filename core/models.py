from django.db import models
from django.contrib.auth.models import User

class ProjectForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Each user has one form
    project_name = models.CharField(max_length=255, blank=True, null=True)
    portfolio_operations = models.CharField(max_length=255, blank=True, null=True)
    it_project_manager = models.CharField(max_length=255, blank=True, null=True)
    critical_project = models.BooleanField(default=False)
    it_service_owner_manager = models.CharField(max_length=255, blank=True, null=True)
    budget_owner = models.CharField(max_length=255, blank=True, null=True)
    business_sponsor = models.CharField(max_length=255, blank=True, null=True)
    project_budget = models.CharField(max_length=255, blank=True, null=True)
    business_owner = models.CharField(max_length=255, blank=True, null=True)
    it_pmo = models.CharField(max_length=255, blank=True, null=True)

    project_start_date = models.DateField(blank=True, null=True)
    project_finish_date = models.DateField(blank=True, null=True)

    project_description = models.TextField(blank=True, null=True)
    business_value = models.TextField(blank=True, null=True)
    roi = models.CharField(max_length=255, blank=True, null=True) 
    project_scope = models.TextField(blank=True, null=True)
    constraints = models.TextField(blank=True, null=True)
    vendor_service_support = models.TextField(blank=True, null=True)

    # Delivrabels tabel

    dev_first_name = models.CharField(max_length=255, blank=True, null=True)
    dev_first_date = models.DateField(blank=True, null=True)

    dev_second_name = models.CharField(max_length=255, blank=True, null=True)
    dev_second_date = models.DateField(blank=True, null=True)

    dev_third_name = models.CharField(max_length=255, blank=True, null=True)
    dev_third_date = models.DateField(blank=True, null=True)

    dev_fourth_name = models.CharField(max_length=255, blank=True, null=True)
    dev_fourth_date = models.DateField(blank=True, null=True)

    dev_fifth_name = models.CharField(max_length=255, blank=True, null=True)
    dev_fifth_date = models.DateField(blank=True, null=True)

    dev_sixth_name = models.CharField(max_length=255, blank=True, null=True)
    dev_sixth_date = models.DateField(blank=True, null=True)

    # Extra Delivrabels

    dev_extra_name_1 = models.CharField(max_length=255, blank=True, null=True)
    dev_extra_date_1 = models.DateField(blank=True, null=True)

    dev_extra_name_2 = models.CharField(max_length=255, blank=True, null=True)
    dev_extra_date_2 = models.DateField(blank=True, null=True)

    dev_extra_name_3 = models.CharField(max_length=255, blank=True, null=True)
    dev_extra_date_3 = models.DateField(blank=True, null=True)

    dev_extra_name_4 = models.CharField(max_length=255, blank=True, null=True)
    dev_extra_date_4 = models.DateField(blank=True, null=True)

    dev_extra_name_5 = models.CharField(max_length=255, blank=True, null=True)
    dev_extra_date_5 = models.DateField(blank=True, null=True)

    dev_extra_name_6 = models.CharField(max_length=255, blank=True, null=True)
    dev_extra_date_6 = models.DateField(blank=True, null=True)

    dev_extra_name_7 = models.CharField(max_length=255, blank=True, null=True)
    dev_extra_date_7 = models.DateField(blank=True, null=True)

    dev_extra_name_8 = models.CharField(max_length=255, blank=True, null=True)
    dev_extra_date_8 = models.DateField(blank=True, null=True)

    dev_extra_name_9 = models.CharField(max_length=255, blank=True, null=True)
    dev_extra_date_9 = models.DateField(blank=True, null=True)

    dev_extra_name_10 = models.CharField(max_length=255, blank=True, null=True)
    dev_extra_date_10 = models.DateField(blank=True, null=True)

    # Initial Project Plan

    first_task_name = models.CharField(max_length=255, blank=True, null=True)
    first_task_duration = models.CharField(max_length=50, blank=True, null=True)
    first_task_starting = models.DateField(blank=True, null=True)
    first_task_ending = models.DateField(blank=True, null=True)

    second_task_name = models.CharField(max_length=255, blank=True, null=True)
    second_task_duration = models.CharField(max_length=50, blank=True, null=True)
    second_task_starting = models.DateField(blank=True, null=True)
    second_task_ending = models.DateField(blank=True, null=True)

    third_task_name = models.CharField(max_length=255, blank=True, null=True)
    third_task_duration = models.CharField(max_length=50, blank=True, null=True)
    third_task_starting = models.DateField(blank=True, null=True)
    third_task_ending = models.DateField(blank=True, null=True)

     # Extra Task

    task_name_extra_1 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_1 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_1 = models.DateField(blank=True, null=True)
    task_ending_extra_1 = models.DateField(blank=True, null=True)

    task_name_extra_2 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_2 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_2 = models.DateField(blank=True, null=True)
    task_ending_extra_2 = models.DateField(blank=True, null=True)

    task_name_extra_3 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_3 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_3 = models.DateField(blank=True, null=True)
    task_ending_extra_3 = models.DateField(blank=True, null=True)

    task_name_extra_4 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_4 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_4 = models.DateField(blank=True, null=True)
    task_ending_extra_4 = models.DateField(blank=True, null=True)

    task_name_extra_5 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_5 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_5 = models.DateField(blank=True, null=True)
    task_ending_extra_5 = models.DateField(blank=True, null=True)

    task_name_extra_6 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_6 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_6 = models.DateField(blank=True, null=True)
    task_ending_extra_6 = models.DateField(blank=True, null=True)

    task_name_extra_7 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_7 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_7 = models.DateField(blank=True, null=True)
    task_ending_extra_7 = models.DateField(blank=True, null=True)

    task_name_extra_8 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_8 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_8 = models.DateField(blank=True, null=True)
    task_ending_extra_8 = models.DateField(blank=True, null=True)

    task_name_extra_9 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_9 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_9 = models.DateField(blank=True, null=True)
    task_ending_extra_9 = models.DateField(blank=True, null=True)

    task_name_extra_10 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_10 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_10 = models.DateField(blank=True, null=True)
    task_ending_extra_10 = models.DateField(blank=True, null=True)

    task_name_extra_11 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_11 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_11 = models.DateField(blank=True, null=True)
    task_ending_extra_11 = models.DateField(blank=True, null=True)

    task_name_extra_12 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_12 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_12 = models.DateField(blank=True, null=True)
    task_ending_extra_12 = models.DateField(blank=True, null=True)

    task_name_extra_13 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_13 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_13 = models.DateField(blank=True, null=True)
    task_ending_extra_13 = models.DateField(blank=True, null=True)

    task_name_extra_14 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_14 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_14 = models.DateField(blank=True, null=True)
    task_ending_extra_14 = models.DateField(blank=True, null=True)

    task_name_extra_15 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_15 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_15 = models.DateField(blank=True, null=True)
    task_ending_extra_15 = models.DateField(blank=True, null=True)

    task_name_extra_16 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_16 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_16 = models.DateField(blank=True, null=True)
    task_ending_extra_16 = models.DateField(blank=True, null=True)

    task_name_extra_17 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_17 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_17 = models.DateField(blank=True, null=True)
    task_ending_extra_17 = models.DateField(blank=True, null=True)

    task_name_extra_18 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_18 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_18 = models.DateField(blank=True, null=True)
    task_ending_extra_18 = models.DateField(blank=True, null=True)

    task_name_extra_19 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_19 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_19 = models.DateField(blank=True, null=True)
    task_ending_extra_19 = models.DateField(blank=True, null=True)

    task_name_extra_20 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_20 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_20 = models.DateField(blank=True, null=True)
    task_ending_extra_20 = models.DateField(blank=True, null=True)

    task_name_extra_21 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_21 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_21 = models.DateField(blank=True, null=True)
    task_ending_extra_21 = models.DateField(blank=True, null=True)

    task_name_extra_22 = models.CharField(max_length=255, blank=True, null=True)
    task_duration_extra_22 = models.CharField(max_length=50, blank=True, null=True)
    task_starting_extra_22 = models.DateField(blank=True, null=True)
    task_ending_extra_22 = models.DateField(blank=True, null=True)

    


    # Risks & Issues


    first_risk_name = models.CharField(max_length=255, blank=True, null=True)
    first_risk_summary = models.TextField(blank=True, null=True)
    first_risk_date = models.DateField(blank=True, null=True)
    first_risk_sevirity = models.CharField(max_length=255, blank=True, null=True)
    first_risk_mitigation = models.TextField(blank=True, null=True)

    second_risk_name = models.CharField(max_length=255, blank=True, null=True)
    second_risk_summary = models.TextField(blank=True, null=True)
    second_risk_date = models.DateField(blank=True, null=True)
    second_risk_sevirity = models.CharField(max_length=255, blank=True, null=True)
    second_risk_mitigation = models.TextField(blank=True, null=True)

    third_risk_name = models.CharField(max_length=255, blank=True, null=True)
    third_risk_summary = models.TextField(blank=True, null=True)
    third_risk_date = models.DateField(blank=True, null=True)
    third_risk_sevirity = models.CharField(max_length=255, blank=True, null=True)
    third_risk_mitigation = models.TextField(blank=True, null=True)



    risk_name_1 = models.CharField(max_length=255, blank=True, null=True)
    risk_summary_1 = models.TextField(blank=True, null=True)
    risk_date_1 = models.DateField(blank=True, null=True)
    risk_sevirity_1 = models.CharField(max_length=255, blank=True, null=True)
    risk_mitigation_1 = models.TextField(blank=True, null=True)

    risk_name_2 = models.CharField(max_length=255, blank=True, null=True)
    risk_summary_2 = models.TextField(blank=True, null=True)
    risk_date_2 = models.DateField(blank=True, null=True)
    risk_sevirity_2 = models.CharField(max_length=255, blank=True, null=True)
    risk_mitigation_2 = models.TextField(blank=True, null=True)


    risk_name_3 = models.CharField(max_length=255, blank=True, null=True)
    risk_summary_3 = models.TextField(blank=True, null=True)
    risk_date_3 = models.DateField(blank=True, null=True)
    risk_sevirity_3 = models.CharField(max_length=255, blank=True, null=True)
    risk_mitigation_3 = models.TextField(blank=True, null=True)



    # Stakeholders

    stack_first_name = models.CharField(max_length=255, blank=True, null=True)
    stack_first_department = models.CharField(max_length=255, blank=True, null=True)
    stack_first_role = models.CharField(max_length=255, blank=True, null=True)

    stack_second_name = models.CharField(max_length=255, blank=True, null=True)
    stack_second_department = models.CharField(max_length=255, blank=True, null=True)
    stack_second_role = models.CharField(max_length=255, blank=True, null=True)

    stack_third_name = models.CharField(max_length=255, blank=True, null=True)
    stack_third_department = models.CharField(max_length=255, blank=True, null=True)
    stack_third_role = models.CharField(max_length=255, blank=True, null=True)

    stack_fourth_name = models.CharField(max_length=255, blank=True, null=True)
    stack_fourth_department = models.CharField(max_length=255, blank=True, null=True)
    stack_fourth_role = models.CharField(max_length=255, blank=True, null=True)


    stack_name_extra_1 = models.CharField(max_length=255, blank=True, null=True)
    stack_department_extra_1 = models.CharField(max_length=255, blank=True, null=True)
    stack_role_extra_1 = models.CharField(max_length=255, blank=True, null=True)

    stack_name_extra_2 = models.CharField(max_length=255, blank=True, null=True)
    stack_department_extra_2 = models.CharField(max_length=255, blank=True, null=True)
    stack_role_extra_2 = models.CharField(max_length=255, blank=True, null=True)

    stack_name_extra_3 = models.CharField(max_length=255, blank=True, null=True)
    stack_department_extra_3 = models.CharField(max_length=255, blank=True, null=True)
    stack_role_extra_3 = models.CharField(max_length=255, blank=True, null=True)

    stack_name_extra_4 = models.CharField(max_length=255, blank=True, null=True)
    stack_department_extra_4 = models.CharField(max_length=255, blank=True, null=True)
    stack_role_extra_4 = models.CharField(max_length=255, blank=True, null=True)

    stack_name_extra_5 = models.CharField(max_length=255, blank=True, null=True)
    stack_department_extra_5 = models.CharField(max_length=255, blank=True, null=True)
    stack_role_extra_5 = models.CharField(max_length=255, blank=True, null=True)


    # Governance
    PLAN_CHOICES = [
        ('weekly', 'Weekly'),
        ('biweekly', 'Biweekly'),
        ('monthly', 'Monthly'),
    ]

    c_plan = models.CharField(
        max_length=255,
        choices=PLAN_CHOICES,
        blank=True,
        null=True
    )
    ms_project = models.CharField(max_length=255, blank=True, null=True)
    project_report = models.CharField(max_length=255, blank=True, null=True)


    # Approvals
    business_name = models.CharField(max_length=255, blank=True, null=True)
    business_sig = models.FileField(upload_to='signatures/', blank=True, null=True)

    it_project_manager = models.CharField(max_length=255, blank=True, null=True)
    it_project_manager_sig = models.FileField(upload_to='signatures/', blank=True, null=True)

    it_service_owner_manager = models.CharField(max_length=255, blank=True, null=True)
    it_service_owner_manager_sig = models.FileField(upload_to='signatures/', blank=True, null=True)

    it_business_partener = models.CharField(max_length=255, blank=True, null=True)
    it_business_partener_sig = models.FileField(upload_to='signatures/', blank=True, null=True)

    it_pmo_manager = models.CharField(max_length=255, blank=True, null=True)
    it_pmo_manager_sig = models.FileField(upload_to='signatures/', blank=True, null=True)
    
    # Project Closure - General Information
    cl_project_name = models.CharField(max_length=255, blank=True, null=True)
    cl_project_manager = models.CharField(max_length=255, blank=True, null=True)
    
    cl_actual_start_date = models.DateField(blank=True, null=True)
    cl_actual_finish_date = models.DateField(blank=True, null=True)
    
    cl_reason_status = models.CharField(max_length=255, blank=True, null=True)
    cl_reason_status_reason = models.CharField(max_length=255, blank=True, null=True)
    
    # Project Closure - Actual Deliverables
    
    
    cl_actual_d_1 = models.CharField(max_length=255, blank=True, null=True)
    cl_actual_d_2 = models.CharField(max_length=255, blank=True, null=True)
    cl_actual_d_3 = models.CharField(max_length=255, blank=True, null=True)
    cl_actual_d_4 = models.CharField(max_length=255, blank=True, null=True)
    cl_actual_d_5 = models.CharField(max_length=255, blank=True, null=True)
    cl_actual_d_6 = models.CharField(max_length=255, blank=True, null=True)
    cl_actual_d_7 = models.CharField(max_length=255, blank=True, null=True)
    cl_actual_d_8 = models.CharField(max_length=255, blank=True, null=True)
    cl_actual_d_9 = models.CharField(max_length=255, blank=True, null=True)
    cl_actual_d_10 = models.CharField(max_length=255, blank=True, null=True)
    
    # Project Closure - CRs
    
    cl_cr_name1 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost1 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name2 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost2 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name3 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost3 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name4 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost4 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name5 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost5 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name6 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost6 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name7 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost7 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name8 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost8 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name9 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost9 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name10 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost10 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name11 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost11 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name12 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost12 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name13 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost13 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name14 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost14 = models.CharField(max_length=255, blank=True, null=True)

    cl_cr_name15 = models.CharField(max_length=255, blank=True, null=True)
    cl_cost15 = models.CharField(max_length=255, blank=True, null=True)
    
    # Project Closure - Lessons Learned
    
    cl_des1 = models.CharField(max_length=255, blank=True, null=True)
    cl_imp1 = models.CharField(max_length=255, blank=True, null=True)
    cl_ana1 = models.CharField(max_length=255, blank=True, null=True)
    cl_re1 = models.CharField(max_length=255, blank=True, null=True)
    
    cl_des2 = models.CharField(max_length=255, blank=True, null=True)
    cl_imp2 = models.CharField(max_length=255, blank=True, null=True)
    cl_ana2 = models.CharField(max_length=255, blank=True, null=True)
    cl_re2 = models.CharField(max_length=255, blank=True, null=True)
    
    cl_des3 = models.CharField(max_length=255, blank=True, null=True)
    cl_imp3 = models.CharField(max_length=255, blank=True, null=True)
    cl_ana3 = models.CharField(max_length=255, blank=True, null=True)
    cl_re3 = models.CharField(max_length=255, blank=True, null=True)
    
    




    

    


    progress = models.IntegerField(default=0)  # Store progress percentage

    # **Field Weights (Score per Field)**
    FIELD_WEIGHTS = {
        "project_name": 1,
        # "portfolio_operations": 1,
        "it_project_manager": 1,
        "critical_project": 1,
        "it_service_owner_manager": 1,
        # "budget_owner": 5,
        # "business_sponsor": 10,
        # "project_budget": 10,
        # "business_owner": 5,
        "project_start_date": 4,
        "project_finish_date": 4,
        "project_description": 3,
        # "business_value": 10,
        # "roi": 10,
        "project_scope": 3,
        # "constraints": 5,
        # "vendor_service_support": 5,
        # ##################################

        "dev_first_name": 2,
        "dev_first_date": 2,

        # ##################################
        "first_task_name":1.5,
        "first_task_duration":1.5,
        "first_task_starting":1.5,
        "first_task_ending":1.5,

        "second_task_name":1.5,
        "second_task_duration":1.5,
        "second_task_starting":1.5,
        "second_task_ending":1.5,

        "third_task_name":1.5,
        "third_task_duration":1.5,
        "third_task_starting":1.5,
        "third_task_ending":1.5,

        # ##################################
        "first_risk_name":1.2,
        "first_risk_summary":1.2,
        "first_risk_date":1.2,
        "first_risk_sevirity":1.2,
        "first_risk_mitigation":1.2,

        "second_risk_name":1.2,
        "second_risk_summary":1.2,
        "second_risk_date":1.2,
        "second_risk_sevirity":1.2,
        "second_risk_mitigation":1.2,


        # ##################################
        "stack_first_name":2,
        "stack_first_department":1,
        "stack_first_role":1,

        # ##################################
        "c_plan":2,
        "ms_project":1,
        "project_report":1,

        # ##################################
        "business_name":1.2,
        "business_sig":1.2,

        "it_project_manager":1.2,
        "it_project_manager_sig":1.2,

        "it_service_owner_manager":1.2,
        "it_service_owner_manager_sig":1.2,

        "it_business_partener":1.2,
        "it_business_partener_sig":1.2,

        "it_pmo_manager":1.2,
        "it_pmo_manager_sig":1.2,
        
        # ##################################
        "cl_project_name":1,
        "cl_project_manager":1,
        
        "cl_actual_start_date":2,
        "cl_actual_finish_date":2,
        
        "cl_reason_status":1,
        "cl_reason_status_reason":1,
        
        # ##################################
        
        "cl_actual_d_1":1,
        "cl_actual_d_2":1,
        
        # ##################################
        
        "cl_cr_name1":2.5,
        "cl_cost1":2.5,
        
        # ##################################
        
        "cl_des1":2,
        "cl_imp1":2,
        "cl_ana3":2,
        "cl_re3":2
        
        
        
        
    }
    
    
    
    

    def calculate_progress(self):
        """Calculate weighted progress based on filled fields."""
        total_score = sum(self.FIELD_WEIGHTS.values())  # Maximum possible score
        print(total_score)
        earned_score = 0

        for field, score in self.FIELD_WEIGHTS.items():
            value = getattr(self, field)

            # Count booleans if True, count non-empty fields
            if isinstance(value, bool):
                if value:
                    earned_score += score
            elif value:
                earned_score += score

        self.progress = (earned_score / total_score) * 100 if total_score > 0 else 0
        
        
    
    ## this function for checking which filed is used to caculate the percentage
    # def calculate_progress(self):
    #     total_score = sum(self.FIELD_WEIGHTS.values())
    #     earned_score = 0

    #     for field, score in self.FIELD_WEIGHTS.items():
    #         value = getattr(self, field)
    #         print(f"{field} = {value} --> ", end='')

    #         if isinstance(value, bool):
    #             if value:
    #                 earned_score += score
    #                 print(f"Added {score}")
    #             else:
    #                 print("Skipped")
    #         elif value:
    #             earned_score += score
    #             print(f"Added {score}")
    #         else:
    #             print("Skipped")

    #     self.progress = (earned_score / total_score) * 100 if total_score > 0 else 0
    #     print(f"Final earned_score = {earned_score}, Total = {total_score}, Progress = {self.progress}")

    
    
    def save(self, *args, **kwargs):
        self.calculate_progress()
        for field in self._meta.fields:
            value = getattr(self, field.name)
            if isinstance(field, models.DateField) and value == "":
                setattr(self, field.name, None)

        
        for field in self._meta.fields:
            value = getattr(self, field.name)
            if isinstance(field, models.CharField) and value is None:
                setattr(self, field.name, '')

        super().save(*args, **kwargs)

  
        
    
    

    def __str__(self):
        return f"{self.user.username} - {self.progress:.2f}%"
