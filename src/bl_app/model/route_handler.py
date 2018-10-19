#Lida com o gerenciamento de rotas, despachando os responsáveis conforme o método HTTP
from model.postman import Postman
from model.getman import Getman

class RouteHandler:
  # classe que define as funções de rota

  def __init__(self):
    #Inicia uma instância de rotas
      self.instance = True

  def test_mc_gee(self, method):
    response = 'Estamos usando %s\n'%(method)
    return response
  
  def make_new_post(self, data):
    #data é o valor de um form em request do Flask
    #write_post formata os dados de forma 'amigável' ao BD
    data = postman.write_post(data) 
    postman.post(data)

  def edit_post(self, post_name, data):
    getman.get_uniqid(post_name)
    updated_post = postman.write_post(data)
    postman.rewrite(post_id, updated_post)

  def get_recent_posts(self, amount=20):
    #Se não definido como parametro, o padrão são 20 posts
    data = getman.get_recents(amount)
    return data

  def get_posts_by_index(self,fro,to):
    #Pega os posts com index de(fro) até (to). Serve para paginação
    data = getman.get_recents(fro,to)
    