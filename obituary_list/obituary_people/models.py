from django.db import models

class AddtoPeople(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    obituary_text = models.TextField(max_length=300)



    def __str__(self):
        return self.title