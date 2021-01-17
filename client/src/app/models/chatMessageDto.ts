export class ChatMessageDto {
    user: string;
    message: string;
    timeSent :  string;

    constructor(user: string, message: string, timestamp: string){
        this.user = user;
        this.message = message;
        this.timeSent = timestamp;

    }
}