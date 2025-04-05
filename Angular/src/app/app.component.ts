import {Component} from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import {MatTabChangeEvent, MatTabsModule} from '@angular/material/tabs';
import {MatToolbarModule} from '@angular/material/toolbar';
import { GuessframeComponent } from "./guessframe/guessframe.component";

@Component({
  selector: 'app-root',
  imports: [MatButtonModule, MatIconModule, MatTabsModule, CommonModule, MatToolbarModule, GuessframeComponent],
  template: `
  <div [ngStyle]="{ 'background-image': myUrl, 'color':textColor}" class="container-fluid text-center main" >
    <div class="row">
      <mat-toolbar>
        <h1 class="centered">Fiakdle</h1>
      </mat-toolbar>
      <div class="col-3">
        <img class="img-fluid pt-5" src="/assets/pub.png"/>
      </div>

      <div class="col-6">
        <app-guessframe/>
      </div>

      <div class="col-3">
        <img class="img-fluid pt-5" src="/assets/pub.png"/>
      </div>
    </div>
  </div>
    
    
  `,
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  myUrl = "url('/assets/background.jpg')"
  textColor = "#FFFFFF"
  iconColor = "#FFFFFF"
  title = 'Konmlebranle';
  hate = ["motards", "enfants", "bébés", "racistes", "pétitions", "FISE", "FISA", "alcooliques", "autres", "beau gosses","gros", "jeunes", "vieux", "rappeurs", "souris", "mecs qui sont pas super sympa"]
  love = ["motards", "enfants", "bébés", "racistes", "pétitions", "FISE", "FISA", "alcooliques", "autres", "beau gosses","gros", "jeunes", "vieux", "rappeurs", "souris", "mecs qui sont pas super sympa"]

  onTabChanged(event : MatTabChangeEvent){
    if(event.index == 0){
      this.myUrl= "url('/assets/hell.png')"
      this.iconColor = "#FFFFFF"
    }else{
      this.myUrl= "url('/assets/heaven.webp')"
      this.iconColor = "#000000"
    }
    
    
  }
}
