from flask import Flask
import py_eureka_client.eureka_client as eureka_client
from pyctuator.pyctuator import Pyctuator
from flask_cors import CORS,cross_origin

estados={"sala":"Apagadas/Cerradas","dormitorio":"Apagadas/Cerradas","cocina":"Apagadas/Cerradas"}

rest_port =80
host="iluminacion-webavanzada.herokuapp.com"
app_name="iluminacion"

app = Flask(app_name)
CORS(app,resources={r"/*/*":{"origins":"*"},})

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

eureka_client.init(eureka_server="http://52.73.98.2:8099/eureka",
                   app_name=app_name, instance_port=rest_port,instance_host=host)
Pyctuator(
    app,
    app_name,
    app_description="Control de la iluminación del hogar",
    app_url="http://iluminacion-webavanzada.herokuapp.com",
    pyctuator_endpoint_url="http://iluminacion-webavanzada.herokuapp.com/pyctuator",
    registration_url="http://34.232.227.255:8086/instances"
)
