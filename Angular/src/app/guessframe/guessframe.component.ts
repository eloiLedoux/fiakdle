import {Component} from '@angular/core';
import {FormControl, FormsModule, ReactiveFormsModule} from '@angular/forms';
import {Observable} from 'rxjs';
import {map, startWith} from 'rxjs/operators';
import {MatSlideToggleModule} from '@angular/material/slide-toggle';
import {AsyncPipe} from '@angular/common';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';

export interface Perso {
  image: string;
  name: string;
  manga: string;
}

@Component({
  selector: 'app-guessframe',
  imports: [MatAutocompleteModule, MatInputModule, MatFormFieldModule, MatSlideToggleModule, AsyncPipe],
  template: `
    <div class="row p-5 align-items-center">
      <div class="card p-3 mb-3 text-bg-dark">
        <img src="../assets/frostbutt.webp">
        <mat-form-field class="example-full-width">
          <mat-label>State</mat-label>
          <input matInput
                aria-label="Personnage"
                [matAutocomplete]="auto">
          <mat-autocomplete #auto="matAutocomplete">
            @for (perso of filteredPerso | async; track perso) {
              <mat-option [value]="perso.name">
                <img alt="../assets/namiHead.jpg" class="example-option-img" [src]="perso.image" height="40">
                {{perso.name}} | {{perso.manga}}
              </mat-option>
            }
          </mat-autocomplete>
        </mat-form-field>
      </div>  
      
    </div>
    
  `,
  styles: ``
})
export class GuessframeComponent {
  stateCtrl = new FormControl('');
  filteredPerso: Observable<Perso[]>;

  states: Perso[] = [
    {
      name: 'Nami',
      // https://commons.wikimedia.org/wiki/File:Flag_of_Arkansas.svg
      image: '../assets/namiHead.jpg',
      manga: "One Piece",
    },
    {
      name: 'Robin',
      // https://commons.wikimedia.org/wiki/File:Flag_of_California.svg
      image: '../assets/namiHead.jpg',
      manga: "One Piece",
    },
    {
      name: 'Luffy',
      // https://commons.wikimedia.org/wiki/File:Flag_of_Florida.svg
      image: '../assets/namiHead.jpg',
      manga: "One Piece",
    },
    {
      name: 'Zoro',
      // https://commons.wikimedia.org/wiki/File:Flag_of_Texas.svg
      image: '../assets/namiHead.jpg',
      manga: "One Piece",
    },
  ];

  constructor() {
    this.filteredPerso = this.stateCtrl.valueChanges.pipe(
      startWith(''),
      map(state => (state ? this._filterStates(state) : this.states.slice())),
    );
  }

  private _filterStates(value: string): Perso[] {
    const filterValue = value.toLowerCase();

    return this.states.filter(state => state.name.toLowerCase().includes(filterValue));
  }
}
