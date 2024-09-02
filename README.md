# hooter
Electronic Device to Broadcast Tactical Sounds

Commentary:
Many people reveal their level of recognition with a software service based on their familiarity with the sounds played.
The project aims to encapsulate that functionality via a quick prototype. 

For the m5Stack we neeed to deal with some jankiness, including the spi bus not being reset when the sketch is reloaded, this makes terminal error out
There appears to be a problem in the 5stack core, where playing a sound causes the system to reboot.
I have noticed that it appears to be only certain tones that causes this to happen. 
The prototyping device suffers from the following bug
[https://community.m5stack.com/topic/3894/m5stack-speaker-not-working/3](https://community.m5stack.com/topic/3894/m5stack-speaker-not-working/3)
