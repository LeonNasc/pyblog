#Gerencia as ações CRUD do programa.
from db_manager import DatabaseManager

class Postman:
  def __init__(self):
    self.db_man = DatabaseManager()
    self.db_instance = db_man.getInstance()
    self.connection = db_instance.get_connection('rw')

  def make_new_post(self, data):

    post_name = 'Dummy'

    return post_name

  def edit_post(self, data):

    post_name = 'Dummy'

    return post_name
  
  def delete_post(self, data):

    post_name = 'Dummy'

    return post_name