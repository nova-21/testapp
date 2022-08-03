from flask import Flask
import py_eureka_client.eureka_client as eureka_client
from py_eureka_client import netint_utils

estados={"sala":"Apagadas/Cerradas","dormitorio":"Apagadas/Cerradas","cocina":"Apagadas/Cerradas"}
rest_port =80

host="iluminacion-webavanzada.herokuapp.com"
eureka_client.init(eureka_server="http://52.73.98.2:8099/eureka",
                   app_name="iluminacion", instance_port=rest_port,instance_host=host)

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