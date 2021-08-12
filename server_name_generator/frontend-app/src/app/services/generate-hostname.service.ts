import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})

export class GenerateHostnameService {

  constructor(
    private http: HttpClient, private cookieService: CookieService) { }

  // submitForm() {
  //   var formData: any = new FormData();
  //   formData.append("name", this.form.get('name').value);
  //   formData.append("avatar", this.form.get('avatar').value);

  //   return this.http.post<any>(`${environment.apiUrl}/create_string`, formData).subscribe(
  //     (response) => console.log(response),
  //     (error) => console.log(error)
  //   )
  // }
}
