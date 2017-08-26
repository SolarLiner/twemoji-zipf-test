# Twemoji and the Zipf law
  
  
* [Twemoji and the Zipf law](#twemoji-and-the-zipf-law )
	* [Preface](#preface )
		* [The Zipf law?](#the-zipf-law )
			* [It's "everywhere"](#its-everywhere )
			* [Emoji and Zipf's law](#emoji-and-zipfs-law )
	* [The experiment](#the-experiment )
		* [Getting data from Twitter](#getting-data-from-twitter )
		* [Processing data from Twitter](#processing-data-from-twitter )
* [Project Log](#project-log )
	* [Day 1: Starting the project... by doing something else.](#day-1-starting-the-project-by-doing-something-else )
	* [Day 2: Nodejs x Twitter themed allnighter](#day-2-nodejs-x-twitter-themed-allnighter )
		* [Actually coding...](#actually-coding )
  
## Preface
  
  
I've recently came across the Twemoji tracker from a [Vsauce DONG](https://www.youtube.com/watch?v=d1RPFzZN3Ro ) and marvelled at all the real-time, flashing lights of emojis being used all over twitter. But then as I looked at the pattern my subconscious started screaming "ZIPF Law!". That is, indeed, a weird thing to scream; but this is what got me started on this journey. I started wondering about the frequency at which they were used.
  
At the time of writing, the *face with tears or joy emoji* 😂 is the most used emoji on [Emoji tracker](http://emojitracker.com ), and also is the most frequently sent.
  
### The Zipf law?
  
  
> Zipf's law states that given some corpus of natural language utterances, the frequency of any word is inversely proportional to its rank in the frequency table.
  
This quote from the [Wikipedia entry on Zipf's law](http://en.wikipedia.org/wiki/Zipf%27s_law ) describes in more mathematical terms that the most used word in a language will be used twice as often as the second-most used word, and three times as often as the third-most used word, and etc.
  
#### It's "everywhere"
  
  
Let's try and see where Zipf's law can be found, starting with the alphabet.  
I've copied the Wikipedia article on [Frequency Analysis](https://en.wikipedia.org/wiki/Frequency_analysis ) (for a bit of sweet irony) and after some processing to reduce the content to only lowercase letters, this is the resulting bar graph:
  
  
Such a high correlation does point a finger right into the relation between numbers.
  
I know, I know, correlation doesn't imply causation. What if this was the result of any large enough set of letters?
  
Here's the same graph but for random data generated from a [random letter sequence generator](http://www.dave-reed.com/Nifty/randSeq.html ):
  
  
You can see there difference without having me to overlap them. In the first graph, the letter `e` is the most used letter of the whole page, with `t` as a second one, then `a`, then `s`, etc. This actually follows English's letter distribution pretty accurately.  
This second set shows `u` to be the most used of the set, which is the 14th most used letter in the plain english set.
  
Does it happen with other languages? Sure.
  
*(Characters taken from the Japanese version of the Frequency Analysis page)*
  
Zipf is everywhere where you can count the frequency of some natural occurence. City populations? Check. Earth quakes numbers and magnetudes? Check and check.
  
#### Emoji and Zipf's law
  
  
*So, do emoji occurences follow Zipf's law?*
  
Well, that's the whole point of this experiment. My hypothesis, when I started this, is that because emoji are a natural occurence (much like the words we write down), their use should follow Zipf's law. 
  
## The experiment
  
  
I believe that Twitter was the service of choice when [Matthew Rothenberg](https://github.com/mroth ) chose to display realtime emoji usage. For one, lots of people are using it. And *a lot of data* is coming in: according to the [Emoji tracker source code](https://github.com/mroth/emojitrack-feeder#development-setup ), Receiving *all the tweets* will take about 1 MB/s of your bandwidth. This is 8 Mbps, or about a decently compressed 720p video streaming from the Internet.
  
I wish I had a server in the cloud to make the computation available without downtime, but for now I don't - so if anyone wants to reproduce this at home, you'll need to have a decent internet connection.
  
### Getting data from Twitter
  
  
This is the easy part. The Twitter Streaming API allows us to recieve all the tweets, in real time. This is the same API that power the emoji tracker, and is the perfect fit for the job.
  
* Note: API keys are not provided in the repository for security purposes. Generate your own and add them to 'api/streaming.json' like so:
  
```json
{
    consumer_key: "your_consumer_key",
    consumer_secret: "your_consumer_secret",
    token: "your_access_token_key",
    token_secret: "your_access_token_secret"
}
```
  
*JSON format is to respect the [`npm twiter-stream-api`](https://www.npmjs.com/package/twitter-stream-api ) `var keys` format.*
  
### Processing data from Twitter
  
  
Now comes the hard part. We need to get the mangled, minified data from the Streaming API and process it to get the message content, and from there, extract the emoji(s).
  
# Project Log
  
  
Here lies my thoughts and notes while building the project.  
As this will surely become longer than the article itself, it will be removed from here. It is already available [here](Project Log.md ).
  
  
  
  
  
  
  
  
## Day 1: Starting the project... by doing something else.
  
  
I started the project after seeing the Emoji tracker website displaying real time data about emoji usage on Twitter. This gave way to this project, made to test the hypothesis that emoji follow Zipf's law.
  
But I didn't really do anything *directly* aimed at the project. I instead started documenting my intentions first, padded with a bit of an explanation for what's what and what's happening. This in turn gave way to an overly long showcase of Zipf's law through character freqyency analysis and usage of Matplotlib - which finally I had a use of. I wanted to work with it quite badly after being first introduced to it. But learning *yet another Python library* takes time and took me away from actually starting building the project. Oh well...
  
## Day 2: Nodejs x Twitter themed allnighter
  
  
I am currently in Vietnam for unrelated matters and my plane back to France is at 8:30am, which, taking a 2 hour buffer just in case + driving there; I need to wake up at 4am tomorrow.  
Screw this "sleeping" thing, the flight will be a long 13 hours cramped in an Economy class seat and I will have time to sleep there.
  
Let's start writing some actual JS code!
  
Or should I say *TS code*, because I'm so fond of scrtict typing that I'm happy to add another compilation step just for it. Plus VS Code is awesome with TS.
  
I'm building the project with Node v8 and TS v2.5. Nodejs stuff is still new to me so I'm bound to making mistakes.
  
Wish me luck...
  
### Actually coding...
  
  
... But only after forcing Git to get his act together. Wasted time for nothing trying to sync the project to GitHub. Oh well, I have (half of) my night for myself.
  
Let's start by defining the processing classes first, this way I can save the headaches of OAuth2 for later.
  
  