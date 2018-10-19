#Lida com o gerenciamento de rotas, despachando os responsáveis conforme o método HTTP

class RouteHandler:
  # classe que define as funções de rota

  def __init__(self):
    #Inicia uma instância de rotas
      self.instance = True

  def test_mc_gee(self, method):
    response = 'Estamos usando %s\n'%(method)
    return response