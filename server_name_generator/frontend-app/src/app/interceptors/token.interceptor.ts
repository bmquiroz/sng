import { Injectable } from "@angular/core";
import { HttpInterceptor, HttpHandler, HttpEvent } from "@angular/common/http";
import { AuthService } from "../services/auth.service";
import { HttpRequest } from '@angular/common/http';
import { Observable } from "rxjs";

@Injectable()
export class TokenInterceptor implements HttpInterceptor {
    constructor(public auth: AuthService) { }

    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

        if (this.auth.isLoggedIn()) {
            request = request.clone({
                setHeaders: {
                    Authorization: `Bearer ${this.auth.getToken()}`
                }
            });
        }

        return next.handle(request);
    }
}