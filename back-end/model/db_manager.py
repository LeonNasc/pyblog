#encoding:utf-8
# Gerencia a conexão com o banco de dados
# deve implementar métodos de leitura 'ro'(somente leitura) e 'rw' (escrita)
# com classes que expandem a funcionalidade de db_manager
from postgres import Postgres

class DatabaseManager:

  __instance = None

  def __init__(self):
    #deve ser acessado somente pelo get_instance
    return None

  @classmethod
  def get_instance(cls):
    if cls.__instance is None:
      cls.__instance = DatabaseManager()
    
    return cls.__instance

  def get_connection(self, access_mode):
    #Utiiiza Connection para criar uma conexão conforme o tipo de conexão
    conn_strat = ConnectionStrategy(access_mode)
    return conn_strat.get_connection()

class ConnectionStrategy:
  '''É uma classe que utiliza o padrão Strategy para definir objetos
  que vão efetivamente lidar com o banco de dados'''

  def __init__(self, strategy):

    db = Postgres('host=172.17.0.2 port=5432 dbname=test connect_timeout=10')
   #IP do BD no container atual. Deve mudar no deploy.
   #TODO: Parametrizar dados de conexão

    if strategy == 'ro':
      #Somente serve para os acessos que usam o método GET
      self.connection = ReadOnlyConnection(db)
    else:
      #É uma conexão exclusiva para métodos POST, PUT e DELETE
      self.connection = ReadWriteConnection(db)

  def get_connection(self):
    return self.connection

class ReadOnlyConnection:
  def __init__(self, database):
    self.type = 'ro'
    self.enquirer = Enquirer(self.type)
    self.db = database

  def get_max_index(self):
      query = self.enquirer.max_id_query()
      return self.db.one(query)

  def get_data(self, params):
    # método de somente leitura. O enquirer monta as queries e passa como params
    query = self.enquirer.select_query(params)
    return self.db.all(query,back_as = dict)
    
class ReadWriteConnection(ReadOnlyConnection):
  def __init__(self, database):
    self.type = 'rw'
    self.enquirer = Enquirer(self.type)
    self.db = database
  
  def post_data(self, params):
    # método de escrita no banco de dados.
    query = self.enquirer.insert_query(params)
    self.db.run(query,back_as = dict)

  def update_data(self, params):
    # método de atualização no banco de dados
    query = self.enquirer.update_query(params)
    self.db.run(query,back_as = dict)

  def delete_data(self, params):
    # método de remoção no banco de dados
    query = self.enquirer.delete_query(params)
    self.db.run(query,back_as = dict)

class Enquirer:
  #lida somente com a montagem de consultas ao BD

  def __init__(self, access_type):
    self.type = access_type
    self.DB_NAME = 'posts'

  def max_id_query(self):
      query = "SELECT MAX(post_id) FROM %s;" % self.DB_NAME

      return query

  ######## Em todos os métodos abaixo, params é dict ########

  def select_query(self, params):
    #método de seleção. Funciona com uma conexão 'ro' ou 'rw'
    #TODO: Transformar params em duplas 'chave=valor'
    query = "SELECT * FROM %s WHERE %s ORDER BY postado_em;" % (self.DB_NAME, params)

    return query
  
  def insert_query(self, params):
    self.check_write_permission()
    #método de inserção. Funciona somente em conexões 'rw'
    #TODO: Transformar params em duas longas strings de chaves e valores
    keys = ','.join(params.keys())
    values = "'"+ "','".join(params.values())+"'"
    query = "INSERT INTO %s (%s,postado_em) VALUES (%s,NOW())" % (self.DB_NAME,keys,values)
  
    return query

  def update_query(self, params):
    self.check_write_permission()
    #método de atualização. Funciona soemnte em conexões 'rw'
    #TODO: Destrinchar os dados de params para o query 
    changes = ''
    for key in params.keys():
       changes = key + "=" + params[key] + ","

    changes = ''.join(list(changes)[:-1])

    query = "UPDATE %s SET %s WHERE post_id= %s" % (self.DB_NAME,changes, params['post_id'])

    return query
    
  def delete_query(self, post_id):
    self.check_write_permission()
    #método de remoção. Funciona somente em conexões 'rw'
    #params é somente o id do post a ser removido
    query = "DELETE FROM %s WHERE post_id=%s" % (self.DB_NAME,post_id)

    return query

  def check_write_permission(self):
    if self.type == 'ro':
      raise 'Access method does not permit this operation'
