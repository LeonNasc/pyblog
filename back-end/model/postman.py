#encoding:utf-8
#Gerencia as ações CRUD do programa.

from model.db_manager import DatabaseManager
from model.parsers import DatabaseParser
from model.mailman import Mailman

class Postman(Mailman):
  def __init__(self):
    self.parser = DatabaseParser()
    self.db = DatabaseManager.get_instance()
    self.connection = self.db.get_connection('rw')
  
  def post_item(self, data):
    #Permite gerar o link unico de cada post
    self.connection.post_data(data)
    link = self.parser.parse_titulo(data['titulo'],self._obtain_title_id(data['titulo']))
    
    #Provavelmente é a pior solução possível reescrever após a inserção
    data['link'] = link
    self.connection.update_data(data) 

    return link

  def edit_item(self,data):

    self.connection.update_data(data)

    return self.parser.parse_titulo(data['titulo'],self._obtain_title_id(data['titulo']))
 
  def delete_item(self, titulo):
#    if (self.isValidPostId(titulo)):
      self.connection.delete_data(self.parser.get_uniqid(titulo))
#    else:
#      raise 'Não foi possível deletar o post'

#    return True

  def _obtain_title_id(self, titulo):
    try: 
        return self.connection.get_data("titulo='%s'" % titulo)['post_id']
    except:
        return 0
 
  def isValidToken(self, data):
    ''' Em docs/docs.md eu defino alguns tokens esperados de passagem, tanto para
    entrada de dados quanto para saída de dados. Aqui, eu utilizo o modelo 
    'postagem' para a passagem de dados '''
    post_schema = ('titulo','autor','conteudo','tags') 
    for attribute in post_schema:
      if attribute not in data.keys():
        return False
    return True
