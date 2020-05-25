from django.db import models

# Create your models here.
class ORMInitiative(models.Model):
    init_id = models.AutoField(primary_key=True)
    acronym = models.CharField(max_length=10, null=True)
    full_name = models.CharField(max_length=30, null=True)
   
    def __str__(self):
        return "{} - {}".format(str(self.acronym), str(self.full_name))

# class ORMSave(models.Model):
#     initiative = models.ForeignKey(ORMInitiative, on_delete=models.CASCADE)

#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = 'Save'
#         verbose_name_plural = 'Saves'

#     def __str__(self):
#         return str(self.initiative)