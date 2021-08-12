import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.scss']
})
export class LandingComponent implements OnInit {

  constructor(
    private router: Router,
    private authenticationService: AuthService
  ) { }

  ngOnInit(): void {
  }

  generate() {
    this.router.navigate(['/generate']);
  }

  search() {
    this.router.navigate(['/search']);
  }

  logout() {
    this.authenticationService.logout()
  }
}
