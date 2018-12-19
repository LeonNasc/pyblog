import { TestBed } from '@angular/core/testing';

import { EnquirerService } from './enquirer.service';

describe('EnquirerService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: EnquirerService = TestBed.get(EnquirerService);
    expect(service).toBeTruthy();
  });
});
