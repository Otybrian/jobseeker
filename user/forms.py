from django import forms
from .models import Employer, Job


# class EmployerInformationForm(forms.ModelForm):
#     class Meta:
#         model = Employer
#         field = ('company_name', 'email', 'company_contact', 'company_location', 'company_bio', 'address', 'company_profile')

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        field = ('title', 'location', 'requirements', 'jobtype')
