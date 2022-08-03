from flask import Flask
import py_eureka_client.eureka_client as eureka_client
from py_eureka_client import netint_utils

estados={"sala":"","dormitorio":"","cocina":""}
rest_port =80


app = Flask(__name__)

@app.post("/iluminacion/<habitacion>/<lumens>/<hora>")
def iluminacion(habitacion,lumens,hora):
    if int(lumens) < 15000:
        if (int(hora) >= 18 or int(hora)<=7):
            estados[habitacion]="Luces encendidas"
            print(estados)
            return estados
        else:
            estados[habitacion] = "Persianas abiertas"
            return estados
    else:
        estados[habitacion] = "Apagadas/Cerradas"
        return estados

@app.get("/iluminacion")
def getIluminacion():
    return estados