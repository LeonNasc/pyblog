#handles the routes for app:

class Routes:
  # classe que define as funções de rota

  def __init__(self):
    #Inicia uma instância de rotas
      self.instance = True

  def home(self):
    return "<h1> Hello World</h1>"

  def test_mc_gee(self, method):
    response = 'Estamos usando %s'%(method)
    return response
    
  def hello(self):
    return "Hello World!!!"