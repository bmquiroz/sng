import { TestBed } from '@angular/core/testing';

import { GenerateHostnameService } from './generate-hostname.service';

describe('GenerateHostnameService', () => {
  let service: GenerateHostnameService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GenerateHostnameService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
