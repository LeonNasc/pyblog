import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminSuiteComponent } from './admin-suite.component';

describe('AdminSuiteComponent', () => {
  let component: AdminSuiteComponent;
  let fixture: ComponentFixture<AdminSuiteComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AdminSuiteComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AdminSuiteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
