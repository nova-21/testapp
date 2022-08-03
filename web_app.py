from flask import Flask
import py_eureka_client.eureka_client as eureka_client
from py_eureka_client import netint_utils

rest_port =80
ip = netint_utils.get_first_non_loopback_ip("192.168.10.0/24")
eureka_client.init(eureka_server="http://52.73.98.2:8099/eureka",
                   app_name="iluminacion", instance_port=rest_port, instance_ip=ip)

app = Flask(__name__)

@app.post("/iluminacion/<lumens>/<hora>")
def iluminacion(lumens,hora):
    if int(lumens) < 15000:
        if (int(hora) >= 18 or int(hora)<=7):
            return "Luces encendidas"
        else:
            return "Persianas abiertas"
    else:
        return "Apagadas/Cerradas"