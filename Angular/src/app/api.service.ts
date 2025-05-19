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

  guess(name : string) : boolean {
    if (name.toLowerCase() == "nami"){
      return true;
    }
    return false;
  }
}
