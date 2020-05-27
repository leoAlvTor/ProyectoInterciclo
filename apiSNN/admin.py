from django.contrib import admin
from apiSNN.models import Libro
from apiSNN.models import Persona
from apiSNN.models import Image
# Register your models here.
admin.site.register(Libro)
admin.site.register(Persona)
admin.site.register(Image)