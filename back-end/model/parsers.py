#encoding:utf-8
#Fornece Parsers para os dados do blog
# 19/10/18: Decidi que vou usar Markdown como linguagem de formatação do blog

import json

class DatabaseParser:

    def __init__(self):
      self.yey = 'yey'

    def to_json(self, data):
     
      for post in data:
        post['postado_em'] = str(post['postado_em'])
        post['editado_em'] = str(post['editado_em'])
            
      return json.dumps(data) 

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
