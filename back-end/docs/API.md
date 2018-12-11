*Ponto de entrada da api será denominado api*

##Create
`api/v1/blog/posts/new`

Cria um post. Todo os posts seguirão uma nomenclatura `nome-do-post-id`,
retornando um link acessível via GET.

##Read
`api/v1/blog/posts/recents`

Obtém a lista dos últimos 20 posts.

`api/v1/blog/posts/<mês>`

Obtém a lista dos posts de <mês>

`api/v1/blog/posts/view/<nome-do-post-id>`

Obtém o post em <nome-do-post-id>

`api/v1/blog/posts/recents_<num1>_<num2>`

Indexa os posts a partir do mais recente e lista de num1 até num2

##Update
`api/v1/blog/posts/view/<nome-do-post-id>/edit`

Permite a edição dos dados de <nome-do-post-id> no banco de dados

##Delete

`api/v1/blog/posts/view/<nome-do-post-id>/delete`

Remove o post <nome-do-post-id>


