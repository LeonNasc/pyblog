# Gerencia a conexão com o banco de dados
# deve implementar métodos de leitura 'ro'(somente leitura) e 'rw' (escrita)
# com classes que expandem a funcionalidade de db_manager

class DatabaseManager:

  __instance = None

  def __init__(self):
    #deve ser acessado somente pelo get_instance
    if DatabaseManager.__instance:
      return self.get_instance()      

  @classmethod
  def get_instance(cls):
    if cls.__instance is None:
      cls.__instance = DatabaseManager()
    
    return cls.__instance

  def get_connection(self, access_mode):
    #Utiiiza Connection para criar uma conexão conforme o tipo de conexão

    return Connection(access_mode)
  

class Connection:
  #É uma classe que utiliza o padrão Strategy para definir objetos
  #que vão efetivamente lidar com o banco de dados

  def __init__(self, strategy):
    if strategy == 'ro':
      #Somente serve para os acessos que usam o método GET
      return ReadOnlyConnection()
    else:
      #É uma conexão exclusiva para métodos POST, PUT e DELETE
      return ReadWriteConnection()

class ReadOnlyConnection:
  def __init__(self):
    #something something BD
    self.initialized = True
    
class ReadWriteConnection:
  def __init__(self):
    #something something BD
    self.initialized = True
