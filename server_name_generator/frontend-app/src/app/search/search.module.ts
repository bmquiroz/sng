import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SearchRoutingModule } from './search-routing.module';
import { SearchComponent } from './search.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { AngularMaterialModule } from 'src/app/angular-material.module';
/* FormsModule */
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [SearchComponent],
  imports: [
    CommonModule,
    SearchRoutingModule,
    FlexLayoutModule,
    AngularMaterialModule,
    FormsModule, 
    ReactiveFormsModule,
  ]
})
export class SearchModule { }
