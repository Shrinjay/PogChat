  
import { Component, OnInit, OnDestroy, ViewChild, ElementRef, AfterViewChecked } from '@angular/core';
import { NgForm } from '@angular/forms';
import {MessageServiceService} from '../message-service.service'
//import { ChatMessageDto } from '../models/chatMessageDto';


// const req = request(
//   {
//     host: 'LINK',
//     path: 'register',
//     method: "GET",
//   },
//   response => {
//     console.log(response.statusCode); //ideally 200

//   }
// );

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit, OnDestroy, AfterViewChecked {

  @ViewChild('scroller') private feedContainer: ElementRef;

  timeStamp: Date = new Date();
  contents = [];
  scrollingElement = document.getElementById('chat-container');
  user_id : any;
  lastName : any;

async sendMessage(sendForm: NgForm){

  sendForm.value.time = this.getTimeStamp();

  console.log(sendForm.value);

  if (!(!!this.user_id) || ((!!this.lastName) && this.lastName!=sendForm.value.user)) this.user_id = await this.register(sendForm)
  this.lastName = sendForm.value.user

  this.messageService.sendMessage({
    ip:"33.248.92.47",
    id:this.user_id
  }, sendForm.value.message, sendForm.value.time).subscribe(e => {
    this.contents=[]
    e.forEach(c => this.contents.push(...c.messages))

  })

  console.log(this.contents)
  


}

register(sendForm) : Promise<any> {
  return new Promise((resolve, reject)=> {
    this.messageService.registerUser({
      ip: "33.248.92.47",
      name: sendForm.value.user
    }).subscribe(e => {
       resolve(e);
    })
  })
  
}



  constructor(private messageService: MessageServiceService) { }

  ngOnInit(): void {

    this.messageService.getMessages({ip: '33.248.92.47'}).subscribe(e => e.forEach(c => this.contents.push(...c.messages)))
    console.log(this.contents)
  }

  ngAfterViewChecked() {
    this.scrollToBottom();
  }

scrollToBottom(): void{
  this.feedContainer.nativeElement.scrollTop = this.feedContainer.nativeElement.scrollHeight;
}

  ngOnDestroy(): void {
    
  }


  getTimeStamp() {
    const now = new Date();
    const date = now.getUTCFullYear() + '/' +
                 (now.getUTCMonth() + 1) + '/' +
                 now.getUTCDate();
    const time = now.getUTCHours() + ':' +
                 now.getUTCMinutes() + ':' +
                 now.getUTCSeconds();

    return (date + ' ' + time);
  }






  }



