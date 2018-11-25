#encoding:utf-8
#Lida com o gerenciamento de rotas, despachando os responsáveis conforme o método HTTP
from model.postman import Postman
from model.getman import Getman

API_ROUTE = 'api/blog/posts'

class RouteHandler:
  # classe que define as funções de rota

  def __init__(self):
    #Inicia uma instância dos gerenciadores de rota
    self.postman = Postman()
    self.getman = Getman()

  def make_new_post(self, data):
    #data é o valor de um form em um request para o Flask
    #write formata os dados de forma 'amigável' ao BD
    data = self.postman.write(data) 
    post_name = self.postman.post(data)

    return '%s/%s' % (API_ROUTE, post_name)

  def edit_post(self, post_name, data):
    post_id = self.getman.get_uniqid(post_name)

    updated_post = self.postman.write(data)
    self.postman.rewrite(post_id, updated_post)

    return '%s/%s' % (API_ROUTE, post_name)

  def delete_post(self,post_name):
    post_id = self.getman.get_uniqid(post_name)
    self.postman.delete(post_id)

    return self.get_recent_posts()

  def get_post_by_id(self,post_name):
    return self.getman.get_post(post_name)
    
  def get_posts_by_date(self,month,year):
    return self.getman.get_monthly_posts(month,year)

  def get_recent_posts(self, amount=20):
    #Se não definido como parametro, o padrão são 20 posts
    recents = self.getman.get_recents(amount)
    return recents

  def get_indexed_recents(self,fro=1,to=20):
    #Pega os posts com index de(fro) até (to). Serve para paginação
    indexed_recents = self.getman.get_indexed(fro,to)
    return indexed_recents 
