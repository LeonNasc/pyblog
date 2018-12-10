#encoding:utf-8
#Implementa todas as funções GET da API

from model.db_manager import DatabaseManager
from model.parsers import DatabaseParser

class Getman:

  def __init__(self):
    self.parser = DatabaseParser()
    self.db = DatabaseManager.get_instance()
    self.connection = self.db.get_connection('ro')  
  
  def get_post(self, post_name):
    post_id = self.parser.get_uniqid(post_name)
    post = self.connection.get_data('post_id=%s'%post_id)
    return self.parser.to_json(post) 

  def get_recents(self, amount=20):
    #pega todos os items
    data = self.connection.get_data('1=1')[:amount]
    
    return self.parser.to_json(data,amount)
  
  def get_indexed(self,fro,to):
    data = self.connection.get_data('post_id>= %s AND post_id <=%s'% (fro,to))

    return self.parser.to_json(data)

  def get_monthly_posts(self, month, year):
      query = "EXTRACT(MONTH FROM postado_em) = %s AND EXTRACT(YEAR FROM postado_em)=%s "%(month,year)
      data = self.connection.get_data(query)
      return self.parser.to_json(data)
