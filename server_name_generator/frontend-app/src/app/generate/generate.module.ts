import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { GenerateRoutingModule } from './generate-routing.module';
import { GenerateComponent } from './generate.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { AngularMaterialModule } from 'src/app/angular-material.module';
/* FormsModule */
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [GenerateComponent],
  imports: [
    CommonModule,
    GenerateRoutingModule,
    FlexLayoutModule,
    AngularMaterialModule,
    FormsModule, 
    ReactiveFormsModule,
  ]
})
export class GenerateModule { }
