import { Component, OnInit } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { PostableComponent } from '../postable/postable.component';
import { EnquirerService } from '../enquirer.service';

@Component({
  selector: 'app-form-post',
  templateUrl: './form-post.component.html',
  styleUrls: ['./form-post.component.css']
})
export class FormPostComponent extends PostableComponent {
	
  // Todos os inputs do formulário são two-way binded a estas variaveis

  constructor(private http:HttpClient,private enquirer:EnquirerService) {super() }

  //Envia um post para o servidor usando o Http service.
  sendPostForm(){

  let httpOptions = this.enquirer.ngSetHeaders();
  let schema = this.ngDefineSchema();

	if(this.isValidSchema(schema)){
		this.http.post(this.base_url+"posts/new",schema,httpOptions).subscribe((data) => console.log(data))
	}
  }
}
