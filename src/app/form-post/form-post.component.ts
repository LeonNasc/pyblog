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
option = {promptURLs: true,
    renderingConfig: {codeSyntaxHighlighting: true},
    showIcons: ['code', 'table'],
    toolbar: [
        'bold',
        'italic',
        'heading',
        'code',
        'quote',
        'unordered-list',
        'ordered-list',
        'table',
        'link',
        'horizontal-rule',
        'preview',
        'side-by-side',
        'fullscreen',
        'guide',
    '|', // Separator
]};


	constructor(private http:HttpClient,private enquirer:EnquirerService) {
		super();
	}

  //Envia um post para o servidor usando o Http service.
  sendPostForm(){ 

  let httpOptions = this.enquirer.ngSetHeaders();
  let schema = this.ngDefineSchema();

	if(this.isValidSchema(schema)){
		this.http.post(this.base_url+"posts/new",schema,httpOptions).subscribe((data) => console.log(data))
		window.location.href= window.location.href.match(/^https?:\/\/[a-z0-9\.]*\/?/)
	}
  }
}
