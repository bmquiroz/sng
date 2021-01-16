import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LandingComponent } from './landing.component';
import { AuthGuard } from '../services/auth.guard';

// const routes: Routes = [{ path: '', component: LandingComponent }];

const routes: Routes = [{
  path: '',
  component: LandingComponent,
  canActivate: [AuthGuard],
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LandingRoutingModule { }
