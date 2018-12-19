import { Component } from '@angular/core';

@Component({
  selector: 'app-postable',
  templateUrl: './postable.component.html',
  styleUrls: ['./postable.component.css']
})
export class PostableComponent{

  private base_url = 'http://172.17.0.2:5000/api/v1/blog/';
  autor:string = ''
  titulo:string = ''
  conteudo:string = ''
  tags:string = ''

  constructor() { }

  ngDefineSchema(){
  // Define um schema para verificar a integridade da informação a ser passada 
  let schema = {"autor":this.autor,
  "titulo":this.titulo,
  "conteudo":this.conteudo,
  "tags":this.tags}
  
    return schema;
  }

//Testa se os dados a serem enviados possuem todos os campos preenchidos
  isValidSchema(schema){
	for(var key in schema){
		if(schema[key]==false)
			return false
	}
	return true;
  }

}
