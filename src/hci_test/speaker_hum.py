from __future__ import division
import re
import sys
import os
import time
from playsound import playsound
from google.cloud import speech
from MicrophoneStream import MicrophoneStream

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


def listen_print_loop(responses, sound):

    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue

        result = response.results[0]
        if not result.alternatives:
            continue

        transcript = result.alternatives[0].transcript

        if '메시지' in transcript or '전화' in transcript or\
           '보여' in transcript or '노래' in transcript or '길' in transcript:
            overwrite_chars = ' ' * (num_chars_printed - len(transcript))
            voice_print = transcript + overwrite_chars
            if not result.is_final:
                sys.stdout.write(voice_print + '\r')
                sys.stdout.flush()

                num_chars_printed = len(transcript)

            else:
                if re.search(r'\b(exit|quit)\b', transcript, re.I):
                    break
                else:
                    print(voice_print)
                    playsound('../../hum_sound/' + sound)
                    time.sleep(2)
                    break
                num_chars_printed = 0


def main():
    global CHUNK
    language_code = 'ko-KR'
    print('AI 스피커가 동작하는데 시간이 걸립니다. 잠시만 기다려 주세요.')
    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results=True)
    playsound('../../open_sound/open.wav')
    print('원하시는 것을 말씀 해주세요.')
    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (speech.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)
        responses = client.streaming_recognize(streaming_config, requests)
        path = r'C:\Users\leewo\hci_test\hum_sound'
        sounds = os.listdir(path)
        for sound in sounds:
            listen_print_loop(responses, sound)


if __name__ == '__main__':
    main()
