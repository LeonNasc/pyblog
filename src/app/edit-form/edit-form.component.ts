import { Component, OnInit } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { EnquirerService } from '../enquirer.service';
import { PostableComponent } from '../postable/postable.component';
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-edit-form',
  templateUrl: './edit-form.component.html',
  styleUrls: ['./edit-form.component.css']
})
export class EditFormComponent extends PostableComponent implements OnInit{

	params;

	constructor(private http:HttpClient,private enquirer:EnquirerService,private route: ActivatedRoute) { 
		super();
		this.route.params.subscribe( params => this.params = params );	
	}

  ngOnInit() {
	  let data_fetched = <any>{};
	  this.http.get(this.base_url+"posts/view/"+this.params.id).subscribe((data)=> 
		  {
			data_fetched =  data[0];
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
	  this.http.put(this.base_url+`posts/view/${this.params.id}/edit`,schema,httpOptions).subscribe((data) => console.log(data))
  }
  else{
	console.log("Erro: Schema Inválido");
  }
	 this.ngOnInit()
}
  ngRenderMd(){
  }
}
