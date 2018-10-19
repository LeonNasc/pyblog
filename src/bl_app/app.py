#Ponto de entrada do sistema. Serve como dispatcher das rotas

from flask import Flask, request
from model.routes import Routes 

app = Flask(__name__)
rt = Routes()

@app.route("/")
def home():
  return rt.home()

@app.route("/route_test")
def route_test():
  return rt.test_mc_gee(request.method)

#As outras rotas ficam abaixo. routes define as funções que serão usadas pela API