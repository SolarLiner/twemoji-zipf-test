export class Tweet {
    timestamp: Date

    constructor(public message: string) {
        this.timestamp = new Date(Date.now());
    }

    public static from_raw(input: string): Tweet {
        
    }
}

export class TweetHandler {
    constructor(public tweet: Tweet) {};

    function 
}