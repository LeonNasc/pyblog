#Ponto de entrada do sistema. Serve como dispatcher das rotas
from flask import Flask, request
from model.route_handler import RouteHandler 

app = Flask(__name__)
rt = RouteHandler()

@app.route("/")
def home():
  return "{'text': 'Rota inválida'}"

@app.route("/blog/posts/recent",methods=['GET'])
def recents():
  return rt.get_recent_posts()

@app.route("/blog/posts/<mes>",methods=['GET'])
def posts_by_month(mes):
  #return rt.get_posts_by_month(mes)
  return 'Retornaria os posts do mês %s do ano atual' % (mes)

@app.route("/blog/posts/<mes>/<ano>",methods=['GET'])
def posts_by_month_year(mes,ano="2018"):
  #return rt.get_posts_by_month(mes)
  return 'Retornaria os posts do mês %s do ano %s' % (mes,ano)

@app.route("/blog/posts/_<nome_id>",methods=['GET'])
def posts_by_id(nome_id):
  return 'Pegaria um post com nome %s' % (nome_id)

@app.route("/route_test/<text>",methods=['GET', 'POST'])
def route_test_2(text):
  return rt.hello(text)

#As outras rotas ficam abaixo. routes define as funções que serão usadas pela API