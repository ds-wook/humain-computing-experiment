# hci_test
## hci final project
### 프로토 타입 제작
- type 1: 기존 음성 스피커 (speaker_err.py)
- type 2: 실질적인 도움 (speaker_hel.py)
- type 3: 과장되지 않은 유머 (speaker_umo.py)
- type 4: 겸손한 태도 (speaker_hum.py)
### Python code로 제작 requirements 작성
``` python
import sys
import os
import time
from playsound import playsound
from google.cloud import speech
import pyaudio
from six.moves import queue
```
Microphone 클래스를 따로 만들어서 모듈화 시킴
