from django.contrib import admin
from .models import Qualification, specializations, Registration

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(specializations)
class SpecializationsAdmin(admin.ModelAdmin):
    list_display = ['name1']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'display_highest_qualification', 'display_specialized_subject']

    def display_highest_qualification(self, obj):
        return obj.highest_qualification.name if obj.highest_qualification else None

    display_highest_qualification.short_description = 'Highest Qualification'

    def display_specialized_subject(self, obj):
        return obj.specialized_subject.name1 if obj.specialized_subject else None

    display_specialized_subject.short_description = 'Specialized Subject'

    