import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http: HttpClient, private cookieService: CookieService) { }

  checkToken() {
    return this.cookieService.check('token');
  }

  getToken() {
    return this.cookieService.get('token');
  }

  login(username: string, password: string) {
    return this.http.post<any>(`${environment.apiUrl}/api/login`, { username, password })
      .pipe(map(user => {
        // Store user details and basic auth credentials in local storage to keep user logged in between page refreshes
        user.authdata = window.btoa(username + ':' + password);
        this.cookieService.set('token', user.token);
        localStorage.setItem('currentUser', JSON.stringify(user));
        // this.currentUserSubject.next(user);
        return user;
      }));
  }

  logout() {
    this.cookieService.delete('token');
    this.cookieService.delete('/');
    // Remove user from local storage to log user out
    localStorage.removeItem('currentUser');
    localStorage.clear();
  }

  isLoggedIn() {
    return this.cookieService.check('token');
  }
}
