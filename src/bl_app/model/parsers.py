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

        result = result + '},'

      return result+"{}]"
