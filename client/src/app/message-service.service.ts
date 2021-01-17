import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MessageServiceService {

  constructor(private http: HttpClient) { }

  getMessages(params) {
    return this.http.get<any>('http://localhost:5000/', {params: params})
  }
  
  sendMessage(params, message, time) {
    return this.http.post<any>('http://localhost:5000/newMessage', {message: message, timestamp: time}, {params: params})
  }

  registerUser(params) {
    return this.http.get<any>('http://localhost:5000/register', {params: params})
  }
}
