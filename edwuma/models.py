from django.db import models
from phone_field import PhoneField

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=50)

class UserProfile(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = PhoneField(blank = True)
    location  = models.CharField(max_length=50)
    bio  = models.TextField(max_length=50)
    registration_date = models.DateField(auto_now = False, auto_now_add = False)
    picture = models.ImageField(height_field=None , width_field=None, max_length= 2000)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

class UserAccount(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Job(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    budget = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    created_date = models.DateField(auto_now=False, auto_now_add=False)
    updated_date = models.DateField(auto_now=False, auto_now_add=False)

class SkillCategory(models.Model):
    category_name = models.CharField(max_length=50)

class Certificate(models.Model):
    certificate_name = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    date_earned = models.DateField(auto_now=False, auto_now_add=False)
    updated_date = models.DateField(auto_now=False, auto_now_add=False)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class FreelancerSkill(models.Model):
    created_date = models.DateField(auto_now=False, auto_now_add=False)
    updated_date = models.DateField(auto_now=False, auto_now_add=False)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class FreelancerPayment(models.Model):
    amount = models.CharField(max_length=20)
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
    payment_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class ClientPayment(models.Model):
    amount = models.CharField(max_length=20)
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
    payment_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class LoggingInfo(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    activity = models.TextField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)


class JobProposal(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    freelancer_comment = models.TextField(max_length=255)


class Skill(models.Model):
    skillname = models.CharField(max_length=50)
    skill_category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

class Attachment(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    files = models.CharField(max_length=255)

class JobSkill(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)