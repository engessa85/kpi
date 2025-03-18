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


    def calculate_progress(self):
        total_fields = 17  # Adjust based on actual field count
        filled_fields = 0
        
        for field in self._meta.fields:
            if field.name not in ["id", "user", "progress"]:
                value = getattr(self, field.name)
                if isinstance(value, bool):
                    if value:  # Count booleans if True
                        filled_fields += 1
                elif value:  # Count non-empty fields
                    filled_fields += 1

        self.progress = (filled_fields / total_fields) * 100

    def save(self, *args, **kwargs):
        self.calculate_progress()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.progress:.2f}%"
