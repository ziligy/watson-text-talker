# watson-text-talker

### About
I created this interface for a voice-based-bot that I'm running on a Raspberry Pi 3B. I'm using the AIY Voice HAT, but I was very displeased with the robotic-voice that's supplied by Google. After studying a few other voice options I decided on IBM's Watson because of it's high quality cadence and intonation. I added some features for my purposes and decided others may find some benefit in my effort. The package should work in other internet-connected & sound-output-capable devices.

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
* #### Quiet level
    - optional quiet level factor can be applied to all optional phrases
    - increases or decreases the likelihood that an optional phrase will be voiced
* #### Uses high-quality Waston voices
    - very realistic sounding, with appropriate cadence and intonation
    - voice selection: [see here for selection available](https://www.ibm.com/watson/developercloud/text-to-speech/api/v1/curl.html?curl#get-voice)
    - free tier plan: no credit card required, 10,000 characters per month at no cost

### Voice file cacheing
The package *always* caches new phrases to a file. The cache directory defaults to `./voice_mp3s`, but can also be defined in TT_Config. To regulate the filename I slugify the phrase. This has the advantage of making it human readable. The only caveat is the phrase MUST be limited to 255 characters.

### Phrase grouping
Phrase grouping is based on array of tuples.

```python
    from watson_text_talker import *

    text_talker = TextTalker(username='credentials-username', password='credentials-password')

    importance = TT_Importance()

    grouping_example = [(importance.SAY_30_PERCENT, "I'm your assistant."), (importance.SAY_50_PERCENT, "How are you?"), (importance.SAY_ALWAYS, "Nice to meet you") ]

    text_talker.say_group(grouping_example)
```

Tuples are made up of the importance & the text phrase.

### Importance factors
```python
# TT_Importance is a class of numeric constants
    SAY_ALWAYS = 1
    SAY_90_PERCENT = 2
    SAY_80_PERCENT = 3
    SAY_70_PERCENT = 4
    SAY_60_PERCENT = 5
    SAY_50_PERCENT = 6
    SAY_40_PERCENT = 7
    SAY_30_PERCENT = 8
    SAY_20_PERCENT = 9
    SAY_10_PERCENT = 10
    SAY_NEVER = 11
```

For the same as above we could have just as easily said:
```python
    from watson_text_talker import *

    text_talker = TextTalker(username='credentials-username', password='credentials-password')

    grouping_example = [(8, "I'm your assistant."), (6, "How are you?"), (1, "Nice to meet you") ]

    text_talker.say_group(grouping_example)
```

### Quiet level
The package includes a globally applied `quite level` that increases or decreases the likelihood that an optional phrase will be voiced.

```python
    from watson_text_talker import *

    text_talker = TextTalker(username='credentials-username', password='credentials-password')

    importance = TT_Importance()

    grouping_example = [(importance.SAY_30_PERCENT, "I'm your assistant."), (importance.SAY_ALWAYS, "Nice to meet you") ]

    text_talker.quiet_level = +2

    text_talker.say_group(grouping_example)
```

In the above example the `I'm your assistant` phrase will only be said 10% of the time because of the +2 assigned to quiet level. The `Nice to meet you` is not effected.

### Config
use the TT_Config class to override configuration defaults

```python
# TT_Config's standard defaults

    USERNAME='--watson tts credentials username goes here--'
    PASSWORD='--watson tts credentials password goes here--'

    TTS_VOICE = 'en-US_AllisonVoice'
    TTS_ACCEPT = 'audio/mp3'

    CACHE_DIRECTORY = 'voice_mp3s'
    CACHE_DIRECTORY_IS_RELATIVE = True
    VOICE_FILE_EXTENSION = 'mp3'
```

Use it like so:
```python
    from watson_text_talker import *

    config = TT_Config()
    config.CREDENTIALS_USERNAME='your watson credentials'
    config.CREDENTIALS_PASSWORD='your watson password'
    config.TTS_Voice = 'en-US_MichaelVoice'
    congig.CACHE_DIRECTORY = 'custom_cache'

    text_talker = TextTalker(config=config)

    text_talker.say("Hello world!")
```

### Attributions

* [pygame](https://github.com/pygame/pygame) is used to process the mp3 voice files
* [python-slugify](https://github.com/un33k/python-slugify) is used to create cache file names




