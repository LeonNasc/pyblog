#encoding:utf-8
#Ponto de entrada do sistema. Serve como dispatcher das rotas

from flask import Flask, request
from model.route_handler import RouteHandler 

app = Flask(__name__)
# Permite abstrair o gerenciamento de rotas em outro objeto
rt = RouteHandler()


################## Rotas que não fazem parte da API #####################
@app.route("/<path:dummy>", methods=['POST','GET','PUT','DELETE'])
def not_found(dummy):
  return "{'erro':'Rota %s inválida'}" % (dummy)

########################## Rotas via POST ##############################  
@app.route("/api/v1/blog/posts/new",methods=['POST'])
def make_a_post():
  data = dict(request.form)

  for _input_ in data:
      data[_input_] = data[_input_][0] 

  return rt.make_new_post(data)

########################## Rotas via GET ##############################  
@app.route("/api/v1/blog/posts/recents",methods=['GET'])
def recents():
    return rt.get_recent_posts()

@app.route("/api/v1/blog/posts/recents_<fro>_<to>",methods=['GET'])
def indexed_recents(fro,to):
       #Paginação padrão
       return rt.get_indexed_recents(fro,to)

@app.route("/api/v1/blog/posts/<mes>",methods=['GET'])
def posts_by_month(mes):
  #return rt.get_posts_by_month(mes)
  meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

  if mes not in meses: 
    return not_found('blog/posts/%s' % (mes))

  import datetime as dt

  #Assume que o ano atual deseja ser buscado
  ano = dt.datetime.now().year

  return rt.get_posts_by_date(meses.index(mes)+1,ano)

@app.route("/api/v1/blog/posts/<mes>/<ano>",methods=['GET'])
def posts_by_month_year(mes,ano):
  #return rt.get_posts_by_month(mes)
  return rt.get_posts_by_date(mes,ano)

@app.route("/api/v1/blog/posts/view/<post_id>",methods=['GET'])
def posts_by_id(post_id):
  try:
      return rt.get_post_by_id(post_id)
  except:
      return not_found('view/%s'% post_id)

######################### Rotas via PUT ##############################  
@app.route("/api/v1/blog/posts/view/<post_id>/edit",methods=['PUT'])
def edit_post(post_id):
  try:
      return rt.edit_post(post_id)
  except:
      return not_found('view/%s'% post_id)

######################### Rotas via DELETE ##############################  
@app.route("/api/v1/blog/posts/view/<post_id>/delete",methods=['DELETE'])
def delete_post(post_id):
  try:
      return rt.delete_post(post_id)
  except:
      return not_found('view/%s'% post_id)
