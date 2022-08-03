from flask import Flask

app = Flask(__name__)

@app.post("/iluminacion")
def iluminacion():
    return "Si"