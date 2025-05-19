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
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  animations: []
})
export class AppComponent {
  myUrl = "url('/assets/background.jpg')"
  textColor = "#FFFFFF"
  iconColor = "#FFFFFF"
  title = 'Konmlebranle';
}
