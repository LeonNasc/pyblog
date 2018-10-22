#encoding:utf-8
#Implementa todas as funções GET da API
from model.db_manager import DatabaseManager
from model.parsers import DatabaseParser

class Getman:

  def __init__(self):
    self.parser = DatabaseParser()
    self.db = DatabaseManager.get_instance()

  def get_uniqid(self,post_name):

    return 'Test'
  
  def get_post(self, post_name):

    return 'Test'

  def get_recents(self, amount=20):
    connection = self.db.get_connection('ro')  
    data = connection.get_data('1=1')

    result = '('

    for items in data:
      result = result + "{"
      for k,v in items.items():

         result = result + '%s: %s,' % (k,v)

      result = result + '}<br>'

    result = result + ')'
    return result
  
  def get_indexed(self, fro, to):

    return 'Test'

  def get_monthly_posts(self, month, year):

      return 'Test'
