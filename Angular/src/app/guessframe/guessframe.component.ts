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
import { shakeAnimation, tadaAnimation } from "angular-animations";



@Component({
  selector: 'app-guessframe',
  imports: [ FormsModule, ReactiveFormsModule, MatAutocompleteModule, MatInputModule, MatFormFieldModule, MatSlideToggleModule, AsyncPipe],
  templateUrl: './guessframe.component.html',
  styleUrls: ['./guessframe.component.scss'],
  animations: [
    tadaAnimation(),
    shakeAnimation(),
  ]
})
export class GuessframeComponent {
  persoCtrl = new FormControl<string | Perso>('');
  filteredPerso: Observable<Perso[]>;
  liste: Perso[];
  image : string;
  errorAnimation = false;
  winAnimation = false;
  win=false;
  backgroundColor = "text-bg-dark";

  errorListe : number[] = []

  constructor(private apiService: ApiService) {
    this.liste = this.apiService.getList();
    this.filteredPerso = this.persoCtrl.valueChanges.pipe(
      startWith(''),
      map(value => {
        const name = typeof value === 'string' ? value : value?.name;
        return name ? this._filter(name as string) : [];
      }),
    );
    this.image = this.apiService.getImageOfTheDay();
  }

  private _filter(value: string): Perso[] {
    const filterValue = value.toLowerCase();
    if(value.length <2){
      return [];
    }
    return this.liste.filter(perso => (perso.name.toLowerCase().includes(filterValue) || perso.manga.toLowerCase().includes(filterValue)));
  }

  onSubmit() {
    if(this.persoCtrl.value === null){
      return;
    }
    if( typeof this.persoCtrl.value === 'string'){
      return;
    }
    console.log(this.persoCtrl.value);
    
    var indexPerso = -1;
    for (let index = 0; index < this.liste.length; index++) {
      if(this.liste[index].name.toLowerCase() == this.persoCtrl.value.name.toString().toLowerCase()){
        indexPerso = index;
        break;
      }
    }
    if(indexPerso == -1){
      return;
    }

    var response = this.apiService.guess(this.persoCtrl.value.name);

    if(response == true){
      this.backgroundColor = "text-bg-success";
      this.winAnimation = !this.winAnimation;
      this.win=true;

    }else{
      this.errorAnimation = !this.errorAnimation;
      
      if (this.errorListe.length >=12){
        this.errorListe.pop()
      }
      this.errorListe.unshift(indexPerso);
      
      
    }

    this.persoCtrl.reset();
  }

  displayFonction(perso: Perso){
    if(perso === null){
      return '';
    }
    return perso.name;
  }

}
