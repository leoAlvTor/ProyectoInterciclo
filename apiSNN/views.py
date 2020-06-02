# CONTROLADOR
from django.core.files.storage import FileSystemStorage
from rest_framework import generics  # para microservicio
from apiSNN import models
from apiSNN import serializers
from django.shortcuts import render
import pyrebase  # para consumo servicio base de datos de firebase
from apiSNN.Logica import modeloSNN  # para utilizar modelo SNN
import os
from apiSNN.Logica import modeloCNN
from datetime import datetime


# Create your views here.
class ListLibro(generics.ListCreateAPIView):
    """
    retrieve:
        Retorna una instancia libro.

    list:
        Retorna todos los libros, ordenados por los más recientes.

    create:
        Crea un nuevo libro.

    delete:
        Elimina un libro existente.

    partial_update:
        Actualiza uno o más campos de un libro existente.

    update:
        Actualiza un libro.
    """
    queryset = models.Libro.objects.all()
    serializer_class = serializers.LibroSerializer


class DetailLibro(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Libro.objects.all()
    serializer_class = serializers.LibroSerializer


class ListPersona(generics.ListCreateAPIView):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer


class DetailPersona(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer


config = {

    'apiKey': "AIzaSyDBYpL2tb3yh3SIPo2BFhlS7slKruVGOic",
    'authDomain': "proyectotiendajpri.firebaseapp.com",
    'databaseURL': "https://proyectotiendajpri.firebaseio.com",
    'projectId': "proyectotiendajpri",
    'storageBucket': "proyectotiendajpri.appspot.com",
    'messagingSenderId': "1046831721926",
    'appId': "1:1046831721926:web:7402a636a8cd165f4b16c7",
    'measurementId': "G-MKSCN84RDE"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


class Autenticacion():
    def main_page(request):
        return render(request, "main.html")

    def singIn(request):

        return render(request, "signIn.html")

    def postsign(request):
        email = request.POST.get('email')
        passw = request.POST.get("pass")
        try:
            # user = auth.sign_in_with_email_and_password(email, passw)
            return render(request, "welcome.html")
        except:
            message = "invalid cerediantials"
            return render(request, "signIn.html", {"msg": message})


class Clasificacion():
    file_path = ""
    prediccion = dict()

    def upload_image(request):
        global file_path, prediccion
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if request.method == 'POST':
            print('--' * 20)
            upload_file = request.FILES['elm_img']

            fs = FileSystemStorage()
            dtm = datetime.today()

            leo = str(int(dtm.timestamp()))
            print(leo, '<', '-'*25)
            fs.save(leo+upload_file.name, upload_file)

            file = open(BASE_DIR + '/media/' + leo + upload_file.name, 'r')
            file_path = BASE_DIR + '/media/' + leo + upload_file.name
            print(' -- FIN PROCESO CARGAR -- '*5)
            prediccion = modeloCNN.predecir_imagen(file_path)
            print(prediccion, '<---------------------')
        return render(request, "prediccion.html", {"pred": prediccion.get('pred'), "prob": prediccion.get('prob')})



    def determinarSobrevivencia(request):
        return render(request, "sobrevivencia.html")

    def predecir(request):
        try:
            pclass = int(request.POST.get('pclass'))
            sex = request.POST.get('sex')
            age = int('' + request.POST.get('age'))
            fare = float(request.POST.get('fare'))
            embarked = request.POST.get('embarked')

        except:
            pclass = 2
            sex = 'female'
            age = 60
            fare = 6670
            embarked = 'C'
        print(type(age))
        # resul=modeloSNN.modeloSNN.suma(num1,num2)
        resul = modeloSNN.modeloSNN.predecirSobrevivencia(modeloSNN.modeloSNN, pclass, sex, age, fare, embarked)

        return render(request, "welcome.html", {"e": resul})

