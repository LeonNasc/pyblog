import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EnquirerService {

  constructor() { }

  ngSetHeaders(){
	  //É necessário configurar os headers a serem enviados
	  const httpOptions = {
	  headers: new HttpHeaders({
		    'Content-Type':  'application/json',
		  })
	  };

	  return httpOptions;
  }

}
