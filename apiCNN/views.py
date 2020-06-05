# CONTROLADOR
from django.core.files.storage import FileSystemStorage
from apiCNN.models import Imagen
from django.shortcuts import render
import os
from apiCNN.Logica import modeloCNN
from datetime import datetime


class Initial():
    def main_page(request):
        return render(request, "main.html")


class Clasificacion():
    file_path = ""
    prediccion = dict()

    def upload_image(request):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if request.method == 'POST':
            print('--' * 20)
            upload_file = request.FILES['elm_img']
            nombre = str(upload_file.name)

            fs = FileSystemStorage()
            dtm = datetime.today()

            leo = str(int(dtm.timestamp()))
            fs.save(leo+upload_file.name, upload_file)

            file_path = BASE_DIR + '/media/' + leo + upload_file.name
            print(' -- FIN PROCESO CARGAR -- '*5)
            prediccion = modeloCNN.predecir_imagen(file_path)

            valor_predicho = round(float(prediccion.get('prob')*100), 3)

            db_imagen = Imagen(int(dtm.timestamp()), nombre, prediccion.get('pred'), valor_predicho)
            db_imagen.save()
            valor_predicho = str(valor_predicho) + '%'
        return render(request, "prediccion.html", {"pred": prediccion.get('pred'), "prob": valor_predicho})
