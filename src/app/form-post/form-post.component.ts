import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-form-post',
  templateUrl: './form-post.component.html',
  styleUrls: ['./form-post.component.css']
})
export class FormPostComponent implements OnInit {
	
  // Todos os inputs do formulário são two-way binded a estas variaveis
  autor = '';
  titulo = '';
  conteudo = '';
  tags= '';
	
  test= '';

  constructor(private http:HttpClient) { }

  ngOnInit() {
  }

  ngHttpTest(){
	let url = 'http://172.17.0.2:5000/api/v1/blog/posts/recents';
	let test = this.http.get(url);
	test.subscribe((data) =>this.test = data['posts']);
  }

  //Envia um post para o servidor usando o Http service.
  sendPostForm(){
	//TODO

  }

  
}
