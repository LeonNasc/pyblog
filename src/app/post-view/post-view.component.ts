import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { PostableComponent } from '../postable/postable.component';

@Component({
  selector: 'app-post-view',
  templateUrl: './post-view.component.html',
  styleUrls: ['./post-view.component.css']
})
export class PostViewComponent extends PostableComponent implements OnInit {

	private params;
        public postado_em;

	constructor(private http:HttpClient,private route: ActivatedRoute) {
		super();
		this.route.params.subscribe( params => this.params = params );	
	}

  ngOnInit() {
	  let data_fetched = <any>{};
	  this.http.get(this.base_url+"posts/view/"+ this.params.id).subscribe((data)=> 
		  {
			try{
			data_fetched =  data[0];
			this.autor = data_fetched.autor;
			this.titulo = data_fetched.titulo;
			this.conteudo = data_fetched.conteudo;
			this.tags = data_fetched.tags;
			this.postado_em = data_fetched.postado_em;
			}
			catch(e){
				console.log(e)
			}
		  }
	  )
  }
}
