import { Component, OnInit } from '@angular/core';
import * as OT from '@opentok/client'

@Component({
  selector: 'app-video',
  templateUrl: './video.component.html',
  styleUrls: ['./video.component.css']
})
export class VideoComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    //init opentok obj, publisher, append to publisher element in html

fetch('http://localhost:5000/getSession?ip=129.97.125.3')
.then(res => res.json()
.then(sessionData => {
  var apiKey="47084464"
  console.log(sessionData)
  const session = OT.initSession(apiKey, sessionData.session_id);
  const publisher = OT.initPublisher('publisher');
  
  //event handlers
  session.on({
    //function runs when session.connect() asynchronously completes
    sessionConnected: function(event) {
  
      //publishes & triggers streamCreated clientside
      session.publish(publisher, function(error) {
        if(error) { console.error('Couldn\'t publish the feed, feelsbadman', error); }
      });
    },
  
    //executes when a client joins + publishes their stream
    streamCreated: function(event) {
      //creates container for new subscriber, assigns an id to it -> see html "subscribers"
      let subContainer = document.createElement('div');
      subContainer.id = 'stream-' + event.stream.streamId;
      document.getElementById('subscribers').appendChild(subContainer); //creates div, appends
  
      //subscribes to new stream, sticks it into container
      session.subscribe(event.stream, subContainer, function(error) {
          if(error) { console.error('Couldn\'t subscribe to stream, Sadge', error); }
      });
    }
  });
  
  //connect to session through session object + token
  session.connect(sessionData.token, function(error) {
    if(error) { console.error('Couldn\'t connect to the session, ResidentSleeper', error); }
  });
}))

  }

}
