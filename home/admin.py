from django.contrib import admin
from home.models import *

# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    pass

class WorkExperienceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Skill, SkillAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)