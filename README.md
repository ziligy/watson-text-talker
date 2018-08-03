# watson-text-talker
Python Text-to-Speech Interface using IBM's Watson Text-To-Speech

### Installation

    pip3 install watson-text-talker --user

### Get credentials for Watson Text-To-Speech Lite Version(FREE)  [here](https://console.bluemix.net/catalog/services/text-to-speech)

### Use

```python
from watson_text_talker import *

text_talker = TextTalker(username='your-watson-tts-credentials-username', password='your-watson-tts-credentials-password')

text_talker.say("Hello world!")

