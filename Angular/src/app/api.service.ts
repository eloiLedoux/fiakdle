import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';



export interface Perso {
  image: string;
  name: string;
  manga: string;
}
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseUrl = 'https://placeholder.net';

  liste: Perso[] = [
    {
      name: 'bulma',
      image: 'https://minio-api.letourneur.net/fiakdle/portraits/bulma.png',
      manga: "dragon ball",
    },
    {
      name: 'chisa',
      image: 'https://minio-api.letourneur.net/fiakdle/portraits/chisa.png',
      manga: "grand blue",
    },
    {
      name: 'Nemu',
      image: 'https://minio-api.letourneur.net/fiakdle/portraits/nemu.png',
      manga: "Bleach",
    },
    {
      name: 'rukia',
      image: 'https://minio-api.letourneur.net/fiakdle/portraits/rukia.png',
      manga: "Bleach",
    },
    {
      name: 'Tatsumaki',
      image: 'https://minio-api.letourneur.net/fiakdle/portraits/tatsumaki.png',
      manga: "One punch man",
    },
    {
      name: 'Yoruichi',
      image: 'https://minio-api.letourneur.net/fiakdle/portraits/yoruichi.png',
      manga: "Bleach",
    },
    {
      name: 'Luffy',
      image: 'https://minio-api.letourneur.net/test/luffy.jpg',
      manga: "One Piece",
    },
    {
      name: 'Zoro',
      image: 'https://minio-api.letourneur.net/test/zoro.jpg',
      manga: "One Piece",
    },
    {
      name: 'Nami',
      image: 'https://minio-api.letourneur.net/test/namiHead.jpg',
      manga: "One Piece",
    },
    {
      name: 'Robin',
      image: 'https://minio-api.letourneur.net/test/robin.jpg',
      manga: "One Piece",
    },
    {
      name: 'Luffy',
      image: 'https://minio-api.letourneur.net/test/luffy.jpg',
      manga: "One Piece",
    },
    {
      name: 'Zoro',
      image: 'https://minio-api.letourneur.net/test/zoro.jpg',
      manga: "One Piece",
    },
    {
      name: 'Nami',
      image: 'https://minio-api.letourneur.net/test/namiHead.jpg',
      manga: "One Piece",
    },
    {
      name: 'Robin',
      image: 'https://minio-api.letourneur.net/test/robin.jpg',
      manga: "One Piece",
    },
    {
      name: 'Luffy',
      image: 'https://minio-api.letourneur.net/test/luffy.jpg',
      manga: "One Piece",
    },
    {
      name: 'Zoro',
      image: 'https://minio-api.letourneur.net/test/zoro.jpg',
      manga: "One Piece",
    },
    {
      name: 'Nami',
      image: 'https://minio-api.letourneur.net/test/namiHead.jpg',
      manga: "One Piece",
    },
    {
      name: 'Robin',
      image: 'https://minio-api.letourneur.net/test/robin.jpg',
      manga: "One Piece",
    },
    {
      name: 'Luffy',
      image: 'https://minio-api.letourneur.net/test/luffy.jpg',
      manga: "One Piece",
    },
    {
      name: 'Zoro',
      image: 'https://minio-api.letourneur.net/test/zoro.jpg',
      manga: "One Piece",
    },
    {
      name: 'Nami',
      image: 'https://minio-api.letourneur.net/test/namiHead.jpg',
      manga: "One Piece",
    },
    {
      name: 'Robin',
      image: 'https://minio-api.letourneur.net/test/robin.jpg',
      manga: "One Piece",
    },
    {
      name: 'Luffy',
      image: 'https://minio-api.letourneur.net/test/luffy.jpg',
      manga: "One Piece",
    },
    {
      name: 'Zoro',
      image: 'https://minio-api.letourneur.net/test/zoro.jpg',
      manga: "One Piece",
    },
    {
      name: 'Nami',
      image: 'https://minio-api.letourneur.net/test/namiHead.jpg',
      manga: "One Piece",
    },
    {
      name: 'Robin',
      image: 'https://minio-api.letourneur.net/test/robin.jpg',
      manga: "One Piece",
    },
    {
      name: 'Luffy',
      image: 'https://minio-api.letourneur.net/test/luffy.jpg',
      manga: "One Piece",
    },
    {
      name: 'Zoro',
      image: 'https://minio-api.letourneur.net/test/zoro.jpg',
      manga: "One Piece",
    },
    {
      name: 'Nami',
      image: 'https://minio-api.letourneur.net/test/namiHead.jpg',
      manga: "One Piece",
    },
    {
      name: 'Robin',
      image: 'https://minio-api.letourneur.net/test/robin.jpg',
      manga: "One Piece",
    },
    {
      name: 'Luffy',
      image: 'https://minio-api.letourneur.net/test/luffy.jpg',
      manga: "One Piece",
    },
    {
      name: 'Zoro',
      image: 'https://minio-api.letourneur.net/test/zoro.jpg',
      manga: "One Piece",
    },
  ];

  image : string = "https://minio-api.letourneur.net/test/makima.jpg"

  constructor() {}
  // Get all posts
  getList(): Perso[] {
    return this.liste;
  }

  getImageOfTheDay() : string {
      return this.image;
  }

  guess(perso : Perso) : number {
    if (perso.name.toLowerCase() == "nami"){
      return 1;
    }else if (perso.manga == "One Piece"){
      return 0;
    }
    return -1;
  }

  
}
