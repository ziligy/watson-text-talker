# watson-text-talker
Python Text-to-Speech Interface using IBM's Watson Text-To-Speech

### Installation

    pip3 install watson-text-talker --user

### Get Watson Credentials

#### Sign up for Lite Version(free) Watson Text-To-Speech [here](https://console.bluemix.net/catalog/services/text-to-speech)


### Use

```python
from watson_text_talker import *

text_talker = TextTalker(username='your-watson-tts-credentials-username', password='your-watson-tts-credentials-password')

text_talker.say("Hello world!")

