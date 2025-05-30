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


    # Governance
    c_plan = models.CharField(max_length=255, blank=True, null=True)
    ms_project = models.CharField(max_length=255, blank=True, null=True)
    project_report = models.CharField(max_length=255, blank=True, null=True)


    # Approvals
    business_name = models.CharField(max_length=255, blank=True, null=True)
    business_sig = models.CharField(max_length=255, blank=True, null=True)

    it_project_name = models.CharField(max_length=255, blank=True, null=True)
    it_project_sig = models.CharField(max_length=255, blank=True, null=True)

    it_service_name = models.CharField(max_length=255, blank=True, null=True)
    it_service_sig = models.CharField(max_length=255, blank=True, null=True)

    it_business_name = models.CharField(max_length=255, blank=True, null=True)
    it_business_sig = models.CharField(max_length=255, blank=True, null=True)

    it_pmo_name = models.CharField(max_length=255, blank=True, null=True)
    it_pmo_sig = models.CharField(max_length=255, blank=True, null=True)

    


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

        "it_project_name":1.2,
        "it_project_sig":1.2,

        "it_service_name":1.2,
        "it_service_sig":1.2,

        "it_business_name":1.2,
        "it_business_sig":1.2,

        "it_pmo_name":1.2,
        "it_pmo_sig":1.2,


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

    def save(self, *args, **kwargs):
        self.calculate_progress()
        for field in self._meta.fields:
            value = getattr(self, field.name)
            if isinstance(field, models.DateField) and value == "":
                setattr(self, field.name, None)
        super().save(*args, **kwargs)

  
        
    
    

    def __str__(self):
        return f"{self.user.username} - {self.progress:.2f}%"
