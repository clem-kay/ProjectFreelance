from django.contrib import admin
from .models import Role,UserProfile,LoggingInfo,Job,JobProposal,JobSkill,UserAccount,Skill,SkillCategory,FreelancerSkill,Certificate,ClientPayment,Attachment,FreelancerPayment
# Register your models here.

admin.site.register(Role)
admin.site.register(UserAccount)
admin.site.register(UserProfile)
admin.site.register(LoggingInfo)
admin.site.register(JobSkill)
admin.site.register(Job)
admin.site.register(JobProposal)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(FreelancerPayment)
admin.site.register(FreelancerSkill)
admin.site.register(ClientPayment)
admin.site.register(Certificate)
admin.site.register(Attachment)