import { Component, OnInit } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { PostableComponent } from '../postable/postable.component';


@Component({
  selector: 'app-post-list',
  templateUrl: './post-list.component.html',
  styleUrls: ['./post-list.component.css']
})
export class PostListComponent extends PostableComponent implements OnInit {
	posts = []

	constructor(private http:HttpClient) {
		super();
	}

	ngOnInit() {
	  let data_fetched = <any>{};
	  this.http.get(this.base_url+"posts/recents").subscribe((data)=> 
		  {
			try{
			//Aqui data_fetched é uma lista de posts
			data_fetched =  data;
			this.posts = data_fetched			}
			console.log(this.posts) 
			catch(e){
				console.log(e)
			}
		  }
	  )
  }

}
