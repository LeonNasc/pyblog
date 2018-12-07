#encoding:utf-8
#Gerencia as ações CRUD do programa.
from model.db_manager import DatabaseManager
from model.parsers import DatabaseParser

class Postman:
  def __init__(self):
    self.parser = DatabaseParser()
    self.db = DatabaseManager.get_instance()
    self.connection = self.db.get_connection('rw')
  
  def post(self, data):

    self.connection.post_data(data)
    id_titulo = self.connection.get_data("titulo='%s'" % data['titulo'])

    return self.parser.parse_titulo(data.titulo,id_titulo)
 
  def delete(self, titulo):
    id_post = self.parser.get_uniqid(titulo)
    self.connection.delete(id_post)
    return post_name
 
  def isValidToken(self, data):
    ''' Em docs/docs.md eu defino alguns tokens esperados de passagem, tanto para
    entrada de dados quanto para saída de dados. Aqui, eu utilizo o modelo 
    'postagem' para a passagem de dados '''
    post_schema = ('titulo','autor','conteudo','tags') 
    for attribute in post_schema:
      if attribute not in data.keys():
        return False
    return True
      
      
   