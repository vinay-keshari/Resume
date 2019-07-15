from django.contrib import admin
from .models import profile, AcademicDetail, ProfessionalDetail
# Register your models here.
admin.site.register(profile)
admin.site.register(AcademicDetail)
admin.site.register(ProfessionalDetail)