import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { HeaderComponent } from './header/header.component';
import { ContentComponent } from './content/content.component';
import { MainComponent } from './main/main.component';
import { FormPostComponent } from './form-post/form-post.component';
import { EditFormComponent } from './edit-form/edit-form.component';
import { PostableComponent } from './postable/postable.component';
import { HomeModuleComponent } from './home-module/home-module.component';
import { PostViewComponent } from './post-view/post-view.component';
import { AdminSuiteComponent } from './admin-suite/admin-suite.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

//As rotas da aplicação
const appRoutes: Routes = [
  { path: 'home', component: HomeModuleComponent },
  { path: 'posts/:id',      component: PostViewComponent },
  {
    path: 'admin',
    component: AdminSuiteComponent,
    data: { title: 'Heroes List' }
  },
  { path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  },
  { path: '**', component: PageNotFoundComponent }
]

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    HeaderComponent,
    ContentComponent,
    MainComponent,
    FormPostComponent,
    EditFormComponent,
    PostableComponent,
    HomeModuleComponent,
    PostViewComponent,
    AdminSuiteComponent,
    PageNotFoundComponent,
  ],
  imports: [
    RouterModule.forRoot(appRoutes,{ enableTracing: true }) // <-- debugging purposes only
    ,BrowserModule, HttpClientModule,FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

;
