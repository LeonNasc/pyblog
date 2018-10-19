*Ponto de entrada do app será denominado app*

##Create
`app/blog/posts/new`

Cria um post. Todo os posts seguirão uma nomenclatura `nome-do-post-id`,
retornando um link acessível via GET.

##Read
`app/blog/posts/recent`

Obtém a lista dos últimos 20 posts.

`app/blog/posts/<mês>`

Obtém a lista dos posts de <mês>

`app/blog/posts/<nome-do-post-id>`

Obtém o post em <nome-do-post-id>

##Update
`app/blog/posts/<nome-do-post-id>/edit`

Permite a edição dos dados de <nome-do-post-id> no banco de dados

##Delete

`app/blog/posts/<nome-do-post-id>/delete`

Remove o post <nome-do-post-id>


