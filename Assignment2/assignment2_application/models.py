from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DiseaseType( models.Model ):
    disease_type_id = models.IntegerField()
    description = models.TextField()

class Country( models.Model ):
    cname = models.CharField( max_length = 50 )
    population = models.BigIntegerField()

class Disease( models.Model ):
    disease_code = models.CharField( max_length=50 )
    pathogen = models.CharField( max_length=20 )
    description = models.TextField()
    disease = models.ForeignKey( DiseaseType, on_delete=models.CASCADE )

class Record( models.Model ):
    email = models.ForeignKey( User, on_delete=models.CASCADE )
    cname = models.ForeignKey( Country, on_delete= models.CASCADE )
    disease_code = models.ForeignKey( Disease, on_delete=models.CASCADE)
    total_death = models.IntegerField()
    total_patients = models.IntegerField()


