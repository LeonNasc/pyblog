#Gerencia as ações CRUD do programa.
from model.db_manager import DatabaseManager

class Postman:
  def __init__(self):
    self.db_man = DatabaseManager()
    self.db_instance = self.db_man.get_instance()
    self.connection = self.db_instance.get_connection('rw')

  def write(self, data):

    post_name = 'Dummy'

    return post_name

  def rewrite(self, post_name, data):

    post_name = 'Dummy'

    return post_name
  
  def delete(self, data):

    post_name = 'Dummy'

    return post_name
  
  def post(self, data):
    post_name = 'Dummy'

    return post_name