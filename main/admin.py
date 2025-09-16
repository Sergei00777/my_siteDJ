from django.contrib import admin
from .models import Profile, Experience, Education, Skill, PortfolioItem, Diploma

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession', 'email']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'period']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'specialty', 'period']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']

@admin.register(Diploma)
class DiplomaAdmin(admin.ModelAdmin):
    list_display = ['title', 'institution', 'year']