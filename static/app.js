//init opentok obj, publisher, append to publisher element in html
const session = OT.initSession(apiKey, sessionId);
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
session.connect(token, function(error) {
  if(error) { console.error('Couldn\'t connect to the session, ResidentSleeper', error); }
});