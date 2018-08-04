# watson-text-talker

### About
I created this interface for a voice-based-bot that I'm running on a Raspberry Pi 3B. I'm using the AIY Voice HAT. I was very displeased the robotic-voice that's supplied by Google. After studying a few other voice options I decided on IBM's Waston because of it's high quality cadence and intonation. I added some features for my purposes and decided others may find some benefit in my effort.

### Installation

    pip3 install watson-text-talker --user

### Get [IBM credentials](https://console.bluemix.net/catalog/services/text-to-speech) for Watson Text-To-Speech, Lite Plan is *FREE*

### Simple Use

```python
from watson_text_talker import *

text_talker = TextTalker(username='your-watson-tts-credentials-username', password='your-watson-tts-credentials-password')

text_talker.say("Hello world!")
```

### Features

* #### Voice file cacheing
    - lowers cloud round-trips
    - keeps cost down
* #### Phrase grouping
    - segments phrases/sentences
    - each segment can have it's own importance factor
* #### Importance factors
    - optional percentage chance that a phrase will be voiced
* #### Quiet factor
    - optional quiet factor can be applied to all optional phrases
    - increases or decreases the likelihood that an optional phrase will be voiced
* #### Uses high-quality Waston voices
    - very realistic sounding, with appropriate cadence and intonation
    - voice selection: English(US: 2 female, 1 male), English(UK), Spanish, Japanese, French, German, Spanish (Castilian), Portuguese (Brazil)
    - free tier plan: no credit card required, 10,000 characters per month at no cost

### Voice file cacheing
The package always caches new phrases to a file. The cache directory defaults to `./voice_mp3s`, but can also be defined in TT_Config. To regulate the filename I slugify the phrase. This has the advantage of making it human readable. The only caveat is the phrase MUST be limited to 255 characters. 

### Attributions

* [pygame](https://github.com/pygame/pygame) is used to process the mp3 voice files
* [python-slugify](https://github.com/un33k/python-slugify) is used to create cache file names







    