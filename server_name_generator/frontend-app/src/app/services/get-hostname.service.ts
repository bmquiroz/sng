import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders, } from "@angular/common/http";
import { Observable, of } from 'rxjs';
import { Data } from '../models/data.model';
import { environment } from 'src/environments/environment';

const httpOptions = {
  headers: new HttpHeaders({ 
    'Access-Control-Allow-Origin':'*',
  })
};

@Injectable({
  providedIn: 'root'
})

export class GetHostnameService {

  constructor(private http: HttpClient) { }

  getList(): Observable<Data[]> {
    return this.http.post<Data[]>(`${environment.apiUrl}/api/get_hostnames`, httpOptions);
  }
}
