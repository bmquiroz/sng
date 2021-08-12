import { Component, OnInit } from '@angular/core';
import { NgForm, FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { GenerateHostnameService } from '../services/generate-hostname.service';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../services/auth.service';
import { environment } from 'src/environments/environment';

interface Region {
  value: string;
  viewValue: string;
}

interface Location {
  value: string;
  viewValue: string;
}

interface OS {
  value: string;
  viewValue: string;
}

interface Zone {
  value: string;
  viewValue: string;
}

interface Lifecycle {
  value: string;
  viewValue: string;
}

interface Role {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-generate',
  templateUrl: './generate.component.html',
  styleUrls: ['./generate.component.scss']
})
export class GenerateComponent {
  region: Region[] = [
    { value: 'NA', viewValue: 'NA' },
    { value: 'APAC', viewValue: 'APAC' },
    { value: 'EMEA', viewValue: 'EMEA' },
    { value: 'LATAM', viewValue: 'LATAM' }
  ];
  location: Location[] = [
    { value: 'AWS Cloud', viewValue: 'AWS Cloud' },
    { value: 'Wynyard', viewValue: 'Wynyard' },
    { value: 'Frankfurt', viewValue: 'Frankfurt' },
    { value: 'Atlanta', viewValue: 'Atlanta' }
  ];
  os: OS[] = [
    { value: 'Red Hat', viewValue: 'Red Hat' },
    { value: 'Windows', viewValue: 'Windows' },
    { value: 'SLES', viewValue: 'SLES' },
    { value: 'Other Linux', viewValue: 'Other Linux' }
  ];
  zone: Zone[] = [
    { value: 'Non-DMZ', viewValue: 'Non-DMZ' },
    { value: 'DMZ', viewValue: 'DMZ' }
  ];
  lifecycle: Lifecycle[] = [
    { value: 'Proof of Concept', viewValue: 'Proof of Concept' },
    { value: 'Lab', viewValue: 'Lab' },
    { value: 'Development', viewValue: 'Development' },
    { value: 'Test Quality Assurance', viewValue: 'Test Quality Assurance' },
    { value: 'Stress Performance Load Testing', viewValue: 'Stress Performance Load Testing' },
    { value: 'Quality Control UAT Pre-Prod Staging', viewValue: 'Quality Control UAT Pre-Prod Staging' },
    { value: 'Production', viewValue: 'Production' }
  ];
  role: Role[] = [
    { value: 'Web', viewValue: 'Web' },
    { value: 'Database Oracle', viewValue: 'Database Oracle' },
    { value: 'Database SQL Server', viewValue: 'Database SQL Server' },
    { value: 'Database MySQL', viewValue: 'Database MySQL' },
    { value: 'Database Mongo', viewValue: 'Database Mongo' },
    { value: 'Database DB2', viewValue: 'Database DB2' },
    { value: 'Database Postgres', viewValue: 'Database Postgres' },
    { value: 'Database Hadoop', viewValue: 'Database Hadoop' },
    { value: 'Application', viewValue: 'Application' },
    { value: 'Backup', viewValue: 'Backup' },
    { value: 'Management Monitoring', viewValue: 'Management Monitoring' },
    { value: 'Citrix', viewValue: 'Citrix' },
    { value: 'DWR Domain Controller', viewValue: 'DWR Domain Controller' },
    { value: 'RO Domain Controller', viewValue: 'RO Domain Controller' },
    { value: 'LDAP', viewValue: 'LDAP' },
    { value: 'Google Appliance', viewValue: 'Google Appliance' },
    { value: 'File Server', viewValue: 'File Server' },
    { value: 'Witness', viewValue: 'Witness' },
    { value: 'Config Mgr Site Server', viewValue: 'Config Mgr Site Server' },
    { value: 'Config Mgr Dist Point', viewValue: 'Config Mgr Dist Point' },
    { value: 'Config Mgr Mgt Point', viewValue: 'Config Mgr Mgt Point' },
    { value: 'Config Mgr Cloud Dis Point', viewValue: 'Config Mgr Cloud Dis Point' },
    { value: 'Config Mgr Cloud Proxy', viewValue: 'Config Mgr Cloud Proxy' },
    { value: 'Config Mgr IBCM', viewValue: 'Config Mgr IBCM' }
  ];

  selectedRegion = this.region[0].value;
  selectedLocation = this.location[0].value;
  selectedOS = this.os[0].value;
  selectedZone = this.zone[0].value;
  selectedLifecycle = this.lifecycle[0].value;
  selectedRole = this.role[0].value;

  appIdFormControl = new FormControl('', [
    Validators.required,
  ]);

  descriptionFormControl = new FormControl('', [
    Validators.required,
  ]);

  host;

  items = [];

  valueFromServer: any = null;

  submitted = false;

  constructor(
    private hostnameService: GenerateHostnameService,
    private http: HttpClient,
    private authenticationService: AuthService
  ) {

  }

  form: FormGroup;

  addhost(addhostForm: NgForm) {
    this.submitted = true;
    var formData: any = new FormData();
    formData.append("region", this.selectedRegion);
    formData.append("location", this.selectedLocation);
    formData.append("os", this.selectedOS);
    formData.append("zone", this.selectedZone);
    formData.append("lifecycle", this.selectedLifecycle);
    formData.append("role", this.selectedRole);
    formData.append("app_id", this.appIdFormControl.value);
    formData.append("description", this.descriptionFormControl.value);

    this.http.post(`${environment.apiUrl}/api/create_string`, formData).toPromise().then(response => {
      console.log(response);

      for (let key in response)
        if (response.hasOwnProperty(key))
          this.items.push(response[key]);
    });
  }

  logout() {
    this.authenticationService.logout()
  }
}
