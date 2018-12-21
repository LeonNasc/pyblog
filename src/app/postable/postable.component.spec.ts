import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PostableComponent } from './postable.component';

describe('PostableComponent', () => {
  let component: PostableComponent;
  let fixture: ComponentFixture<PostableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PostableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PostableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
