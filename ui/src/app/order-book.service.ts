import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class OrderBookService {

  constructor(private http: HttpClient) { }

  getBestPrices(): Observable<any> {
      return this.http.get(environment.apiUrl);
  }
}
