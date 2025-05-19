import {Component} from '@angular/core';
import {FormControl, FormsModule, ReactiveFormsModule} from '@angular/forms';
import {Observable} from 'rxjs';
import {filter, map, startWith} from 'rxjs/operators';
import {MatSlideToggleModule} from '@angular/material/slide-toggle';
import {AsyncPipe} from '@angular/common';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import { ApiService } from '../api.service';
import { Perso } from '../api.service';
import { rollInAnimation, shakeAnimation, bounceAnimation, rubberBandAnimation, collapseAnimation } from "angular-animations";



@Component({
  selector: 'app-guessframe',
  imports: [FormsModule, ReactiveFormsModule, MatAutocompleteModule, MatInputModule, MatFormFieldModule, MatSlideToggleModule, AsyncPipe],
  templateUrl: './guessframe.component.html',
  styleUrls: ['./guessframe.component.scss'],
  animations: [
    bounceAnimation({ duration: 2000 }),
    rubberBandAnimation({anchor: 'rubber', direction: '=>', duration: 500}),
    collapseAnimation(),
    shakeAnimation(),
    rollInAnimation()
  ]
})
export class GuessframeComponent {
  persoCtrl = new FormControl('');
  filteredPerso: Observable<Perso[]>;
  liste: Perso[];
  image : string;
  animState = false;

  constructor(private apiService: ApiService) {
    this.liste = this.apiService.getList();
    this.filteredPerso = this.persoCtrl.valueChanges.pipe(
      startWith(''),
      map(str => (str ? this._filter(str) : [])),
    );
    this.image = this.apiService.getImageOfTheDay();
  }

  private _filter(value: string): Perso[] {
    const filterValue = value.toLowerCase();
    if(value.length <2){
      return [];
    }
    return this.liste.filter(state => (state.name.toLowerCase().includes(filterValue) || state.manga.toLowerCase().includes(filterValue)));
  }

  onSubmit() {
    this.animState = true;
    if(this.persoCtrl.value === null){
      return;
    }
    var response = this.apiService.guess(this.persoCtrl.value);
    
    if(response == true){
      console.log("gg");
    }
    this.persoCtrl.reset();
  }

}
