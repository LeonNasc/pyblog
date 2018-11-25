REST é uma estratégia que utiliza o protocolo HTTP para gerar uma interface de acesso
mais prática entre máquinas e usuários.

Existe uma relação 1:1 para as ações CRUD e os métodos HTTP.

1) Create : POST
2) Read : GET
3) Update : PUT
4) Delete : DELETE

Utilizando estes métodos ao enviar mensagens ao servidor, podemos limitar e definir o
que pode ser feito com uma fonte de dados no servidor (BD, arquivos persistentes, etc).

Ele também casa bem com o HTTP ao se lembrar com o conceito de URL (Unique Resource Location),
que permite que cada recurso único tenha um endereço único.

Assim, é bem possível definir uma API que, por exemplo, trabalhe com um objeto no banco de dados
da seguinte forma:

POST .source/api/posts/titulo-do-post-id

Esta requisição serviria por exemplo para enviar uma requisição que geraria um post no banco de
dados do blog. Similarmente,poderiamos ter uma requisição:

GET .source/api/posts/outubro

Que listaria todos os posts do mês de outubro do blog. Também poderíamos ter:

GET .source/api/posts/titulo-do-post-id

Que retornaria o post específico para o front-end.

De outra forma, uma requisição

PUT .source/api/posts/titulo-do-post-id

Serviria para editar ou atualizar o post em questão. Finalmente, se eu desejasse apagar este post
do blog, eu usaria a API da seguinte forma

DELETE .source/api/posts/titulo-do-post-id

Para apagar o post do blog.

A lógica de um servidor que tenha uma postura REST deve implementar a gestão destas requisições.