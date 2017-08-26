import { assert } from "chai";
import { Tweet } from "./tweet";

it('Should create a new message object', () => {
    let tweetObject: Tweet;
    assert.doesNotThrow(() => {
        tweetObject = new Tweet('message');
    })
    assert.isNotNull(tweetObject);
})
it('Should implement timestamps correctly', () => {
    let now = new Date(Date.now());
    let tweetObject = new Tweet('message');
    assert.isAtLeast(tweetObject.timestamp.valueOf(), now.valueOf());
})