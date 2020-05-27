from django.db import models

class Image(models.Model):
    #https://mc.ai/integrar-modelo-de-red-neuronal-convolucional-en-django/
    # file will be uploaded to MEDIA_ROOT / uploads 
    image = models.ImageField(upload_to ='uploads/') 
    # or... 
    # file will be saved to MEDIA_ROOT / uploads / 2015 / 01 / 30 
    # upload = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    label = models.CharField(max_length=20, blank=True)
    probability = models.FloatField()

# Create your models here.
class Libro(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    def __str__(self):
        return self.title

# Create your models here.
class Persona(models.Model):
    #codigo=models.AutoField(primary_key=True)
    pclass = models.IntegerField() #Clase de entrada (Ticket)
    sex = models.CharField(max_length=6) #Genero de la persona
    age = models.IntegerField() #Edad de la persona
    fare = models.FloatField() #El impuesto que pagaron para embarcarse
    embarked = models.CharField(max_length=1) #Puerto de embarque
    survived = models.CharField(max_length=1, blank=True) #Salida, sobrevive=1, no sobrevive=2
    def __str__(self):
        return str(self.pclass) + ':' + self.sex + ':' , str(self.age) + ':' , str(self.fare) + ':' , self.embarked + ':' , str(self.survived)

#MAESTRO DETALLE
"""
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
"""