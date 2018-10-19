#Ponto de entrada do sistema. Serve como dispatcher das rotas
from flask import Flask, request
from model.route_handler import RouteHandler 

app = Flask(__name__)
rt = RouteHandler()


################## Rotas que não fazem parte da API #####################
@app.route("/<path:dummy>", methods=['POST','GET','PUT','DELETE'])
def not_found(dummy):
  return "{'erro':'Rota %s inválida'}" % (dummy)

########################## Rotas via POST ##############################  
@app.route("/blog/posts/new",methods=['POST'])
def make_a_post():
  data = request.data
  return rt.make_new_post(data)

########################## Rotas via GET ##############################  
@app.route("/blog/posts/recent",methods=['GET'])
def recents():
  return rt.get_recent_posts()

@app.route("/blog/posts/recent_<to_fro>",methods=['GET'])
def recents(to_fro):
  #get_indexed_recents indexa os posts por mais recente e retorna um slice
  #com os indexes passados
  separated = lambda x: x.split('_')
  to,fro = separated(to_fro)
  return rt.get_indexed_recents(fro,to)

@app.route("/blog/posts/<mes>",methods=['GET'])
def posts_by_month(mes):
  #return rt.get_posts_by_month(mes)
  meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
  if mes not in meses: 
    return not_found('blog/posts/%s' % (mes))

  return 'Retornaria os posts do mês %s do ano atual' % (mes)

@app.route("/blog/posts/<mes>/<ano>",methods=['GET'])
def posts_by_month_year(mes,ano="2018"):
  #return rt.get_posts_by_month(mes)
  return 'Retornaria os posts do mês %s do ano %s' % (mes,ano)

@app.route("/blog/posts/_<post_id>",methods=['GET'])
def posts_by_id(post_id):
  return 'Pegaria um post com nome %s' % (post_id)

######################### Rotas via PUT ##############################  
@app.route("/blog/posts/_<post_id>/edit",methods=['PUT'])
def edit_post(post_id):
  return 'Editaria um post com nome %s' % (post_id)

######################### Rotas via DELETE ##############################  
@app.route("/blog/posts/_<post_id>/edit",methods=['DELETE'])
def delete_post(post_id):
  return 'Removeria um post com nome %s' % (post_id)
