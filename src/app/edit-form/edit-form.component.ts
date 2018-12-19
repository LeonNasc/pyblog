import { Component, OnInit } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { EnquirerService } from '../enquirer.service';
import { PostableComponent } from '../postable/postable.component';

@Component({
  selector: 'app-edit-form',
  templateUrl: './edit-form.component.html',
  styleUrls: ['./edit-form.component.css']
})
export class EditFormComponent extends PostableComponent implements OnInit{

  constructor(private http:HttpClient,private enquirer:EnquirerService) { super() }

  ngOnInit() {
	let data_fetched;
	  this.http.get(this.base_url+"posts/view/testando-services-do-angular_59").subscribe((data)=> 
		  { 
			data_fetched = data.posts[0]	 	
			this.autor = data_fetched.autor;
			this.titulo = data_fetched.titulo;
			this.conteudo = data_fetched.conteudo;
			this.tags = data_fetched.tags;
		  }
	  )
  }

  sendEditForm(){
  
  let httpOptions = this.enquirer.ngSetHeaders();
  let schema = this.ngDefineSchema();

  if(this.isValidSchema(schema)){
	  this.http.put(this.base_url+"posts/view/testando-services-do-angular_59/edit",schema,httpOptions).subscribe((data) => console.log(data))
  }
  else{
	console.log("Erro: Schema Inválido");
  }
}
  
}
