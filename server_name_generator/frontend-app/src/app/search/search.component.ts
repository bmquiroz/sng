import { Injectable, AfterViewInit, Component, ViewChild, OnInit } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';

import { HttpClient } from "@angular/common/http";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { ActivatedRoute, Router } from "@angular/router";
import { Data } from '../models/data.model';
import { GetHostnameService } from '../services/get-hostname.service';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  response: Data[];

  constructor(
    private gethostnameService: GetHostnameService,
    private authenticationService: AuthService
  ) {
  }

  displayedColumns = ['hostname', 'app_id', 'region', 'description'];

  @ViewChild(MatSort) sort: MatSort;
  @ViewChild(MatPaginator) paginator: MatPaginator;
  dataSource;

  ngOnInit() {
    this.getList();

  }

  getList() {
    this.gethostnameService.getList()
      .subscribe(response => {
        if (!response) {
          return;
        }
        // this.dataSource = response;
        this.dataSource = new MatTableDataSource(response);
        this.dataSource.sort = this.sort;
        this.dataSource.paginator = this.paginator;
      });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

  logout() {
    this.authenticationService.logout()
  }
}
