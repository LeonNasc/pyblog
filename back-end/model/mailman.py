#encoding:utf-8

class Mailman:

    def isValidPostId(self, titulo):

        #Se o titulo é compatível e o id é igual, é o post certo
        post_id = self.parser.get_uniqid(titulo)
        dados = self.connection.get_data('post_id=%s'%post_id)[0]
        titulo_check = titulo == self.parser.parse_titulo(dados['titulo'],post_id)
        id_check = int(dados['post_id']) == int(post_id)

        return titulo_check and id_check