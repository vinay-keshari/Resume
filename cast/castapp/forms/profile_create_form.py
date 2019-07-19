from django import forms
from django.utils.safestring import mark_safe

class ProfileCreateForm(forms.Form):
    first_name  = forms.CharField(label='First Name', max_length=100)
    last_name  = forms.CharField(label='Last Name', max_length=100)
    contact_number = forms.IntegerField(label='Phone Number')
    location = forms.CharField(label='Residence Location', max_length=50)
    email = forms.EmailField(label='Email')
    highschool_name = forms.CharField(label='School Name', max_length=100)
    marks1 = forms.FloatField(label='Marks Obtained')
    CHOICES = [('1', 'marks in cgpa'), ('2', 'marks in percentage')]
    is_cgpa1 = forms.ChoiceField(widget=forms.RadioSelect(), label='', choices=CHOICES)
    inter_school_name = forms.CharField(label='School Name', max_length=100)
    marks2 = forms.FloatField(label='Marks Obtained')
    is_cgpa2 = forms.ChoiceField(widget=forms.RadioSelect(), label='', choices=CHOICES)
    company_name = forms.CharField(label='Company Name', max_length=100)
    designation = forms.CharField(label='Designation', max_length=20)
    join_date = forms.DateField(label='Joining Date')
    last_wd = forms.DateField(label='Last Working Date', required=False)
    certification = forms.CharField(label='Certification', max_length=20)
    valid_from = forms.DateField(label='Valid From')
    valid_till = forms.DateField(label='Valid Till')
    
    
    
