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
    project_start_date = models.DateField(blank=True, null=True)
    project_finish_date = models.DateField(blank=True, null=True)

    project_description = models.TextField(blank=True, null=True)
    business_value = models.TextField(blank=True, null=True)
    roi = models.IntegerField(blank=True, null=True)  # ROI in percentage
    project_scope = models.TextField(blank=True, null=True)
    constraints = models.TextField(blank=True, null=True)
    vendor_service_support = models.TextField(blank=True, null=True)

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
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.progress:.2f}%"
