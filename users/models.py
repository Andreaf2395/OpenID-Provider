from django.db import models
from initiatives.models import ORMInitiative

# Create your models here.
class Email(models.Model):
    email = models.EmailField(primary_key=True)
    token = models.CharField(max_length=1024)
    expiry = models.DateTimeField(auto_now_add=False)

class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    roles = (
    (1,'Student'),(2,'Admin'), (3,'Internal team'), (4,'Teacher') , (5,'Others'),
    )
    type = models.CharField(max_length=30,choices=roles)

    def __str__(self):
        return self.type

class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Skill (models.Model):
    skill_id = models.IntegerField(primary_key=True)
    skill_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.skill_name

class ORMUser(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length = 40)
    last_name =  models.CharField(max_length = 40)
    college_code = models.IntegerField()
    email = models.OneToOneField(Email,on_delete=models.CASCADE)
    email_verified = models.BooleanField()
    role = models.OneToOneField(Role,on_delete=models.CASCADE)
    disable_account = models.BooleanField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)
    user_image = models.ImageField(upload_to=None)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    last_login = models.DateTimeField()
    login_count = models.PositiveIntegerField()
    initiative_associated = models.ManyToManyField(ORMInitiative)

class ORMProject(models.Model):
    proj_id = models.IntegerField()
    proj_name = models.CharField(max_length=50)
    proj_description = models.TextField()
    technology = models.CharField(max_length=200)
    user_id = models.ForeignKey(ORMUser,on_delete = models.CASCADE)