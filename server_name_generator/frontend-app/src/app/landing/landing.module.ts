import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LandingRoutingModule } from './landing-routing.module';
import { LandingComponent } from './landing.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { AngularMaterialModule } from 'src/app/angular-material.module';
/* FormsModule */
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
// import { AuthService } from '../services/auth.service';
import { AuthGuard } from '../services/auth.guard';

@NgModule({
  declarations: [LandingComponent],
  imports: [
    CommonModule,
    LandingRoutingModule,
    FlexLayoutModule,
    AngularMaterialModule,
    FormsModule, 
    ReactiveFormsModule,
  ],
  providers: [AuthGuard],
})
export class LandingModule { }
