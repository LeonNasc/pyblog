#encoding:utf-8
#Implementa todas as funções GET da API
from model.db_manager import DatabaseManager
from model.parsers import DatabaseParser

class Getman:

  def __init__(self):
    self.parser = DatabaseParser()
    self.db = DatabaseManager.get_instance()
    self.connection = self.db.get_connection('ro')  

  def get_uniqid(self,post_name):
    import re
    regex = r'[0-9]+\Z'
    id_getter = re.compile(regex)
    return id_getter.findall(post_name)[0]
  
  def get_post(self, post_name):
    post_id = self.get_uniqid(post_name)
    post = self.connection.get_data('post_id=%s'%post_id)
    return self.parser.to_json(post) 

  def get_recents(self, amount=20):
    #pega todos os items
    data = self.connection.get_data('1=1')
    print(type(data))    
    return self.parser.to_json(data,amount)
  
  def get_indexed(self, fro, to):

    return 'Test'

  def get_monthly_posts(self, month, year):

      return 'Test'
