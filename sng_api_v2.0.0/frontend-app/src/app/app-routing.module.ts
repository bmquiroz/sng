import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthGuard } from './services/auth.guard';

const routes: Routes = [
  { path: '', loadChildren: () => import('./login/login.module').then(m => m.LoginModule) },
  {
    path: 'landing', loadChildren: () => import('./landing/landing.module').then(m => m.LandingModule),
    canActivate: [AuthGuard],
  },
  {
    path: 'generate', loadChildren: () => import('./generate/generate.module').then(m => m.GenerateModule),
    canActivate: [AuthGuard],
  },
  {
    path: 'search', loadChildren: () => import('./search/search.module').then(m => m.SearchModule),
    canActivate: [AuthGuard],
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
