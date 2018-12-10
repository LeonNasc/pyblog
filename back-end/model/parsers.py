#encoding:utf-8
#Fornece Parsers para os dados do blog
# 19/10/18: Decidi que vou usar Markdown como linguagem de formatação do blog

class DatabaseParser:

    def __init__(self):
      self.yey = 'yey'

    def to_json(self, data):
      result = "["
     
      for items in data:
        result = result + "{"

        for k, v in items.items():
          result = result + '%s: %s,' % (k, v)

        result = result + '}'

      return result+']\n'

    def get_uniqid(self,post_name):
      import re
      regex = r'(?<=_)[0-9]+\Z'
      id_getter = re.compile(regex)

      return id_getter.findall(post_name)[0]

    def parse_titulo(self, titulo,id_post):
      nonprint = list('áéíóúÁÉÍÓÚÀÁãõÃÕçÇ,.!?;:')

      for char in nonprint:
        if char in titulo:
          titulo = titulo.replace(char,"")

      titulo = "-".join(titulo.split(" ")[0:5]) + "_"+str(id_post) 

      return titulo.lower()
