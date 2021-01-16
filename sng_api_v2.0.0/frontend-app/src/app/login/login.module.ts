import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoginRoutingModule } from './login-routing.module';
import { LoginComponent } from './login.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { AngularMaterialModule } from 'src/app/angular-material.module';
/* FormsModule */
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [LoginComponent],
  imports: [
    CommonModule,
    LoginRoutingModule,
    FlexLayoutModule,
    AngularMaterialModule,
    FormsModule, 
    ReactiveFormsModule,
  ]
})
export class LoginModule { }
