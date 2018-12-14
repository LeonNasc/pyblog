import { Component, OnInit } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-form-post',
  templateUrl: './form-post.component.html',
  styleUrls: ['./form-post.component.css']
})
export class FormPostComponent {
	
  // Todos os inputs do formulário são two-way binded a estas variaveis
  autor = '';
  titulo = '';
  conteudo = '';
  tags= '';
  private base_url = 'http://172.17.0.2:5000/api/v1/blog/';

  constructor(private http:HttpClient) { }

  ngHttpTest(){
	let test = this.http.get(this.base_url+"posts/recents");
	test.subscribe((data) =>this.autor = data['posts']);
  }

  //Envia um post para o servidor usando o Http service.
  sendPostForm(){

  const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
  })
  };

  let schema = {"autor":this.autor,
  "titulo":this.titulo,
  "conteudo":this.conteudo,
  "tags":this.tags}

	if(this.isValidSchema(schema)){
		this.http.post(this.base_url+"posts/new",schema,httpOptions).subscribe((data) => console.log(data))
	}
  }
  isValidSchema(schema){
	for(var key in schema){
		if(schema[key]==false)
			return false
	}
	return true;
  }  
}
