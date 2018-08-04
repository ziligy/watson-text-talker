# watson-text-talker
Python Text-to-Speech Interface using IBM's Watson Text-To-Speech

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

* Voice file cacheing
    - lowers cloud roundtrips
    - keeps cost down
* Phrase grouping
    - segments phrases/sentences
    - each segment can have it's own importance factor
* Importance factors
    - optional percentage chance that a phrase will be voiced
* Quiet factor
    - optional quiet factor can be applied to all optional phrases
* Uses high-quality Waston voices
    - very realistic sounding, with appropriate cadence and intonation
    - voice selection: English(US: 2 female, 1 male), English(UK), Spanish, Japanese, French, German, Spanish (Castilian), Portuguese (Brazil)
    - free tier plan: no credit card required, 10,000 characters per month at no cost









    