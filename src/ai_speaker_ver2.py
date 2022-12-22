from playsound import playsound
from google.cloud import speech_v1
from google.cloud.speech_v1 import types
import io
import tkinter


def run_quickstart():
    client = speech_v1.SpeechClient()
    # The name of the audio file to transcribe
    file_name = '../../sound/sample.wav'
    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='ko-KR',
        audio_channel_count=2)

    # Detects speech in the audio file
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)

    def closecallback():
        window.destroy()
    window = tkinter.Tk()
    window.title("AI Speaker Test")
    window.geometry("640x400+100+100")
    window.resizable(False, False)
    text = tkinter.Text(window)

    for result in response.results:
        text.insert(tkinter.CURRENT, '음성출력\n')
        if '메시지' in result.alternatives[0].transcript:
            text.insert(tkinter.CURRENT, result.alternatives[0].transcript)
            text.pack()
            button = tkinter.Button(window, text='Close',
                                    command=closecallback)
            button.place(x=0, y=350, relx=0.5)
            window.mainloop()
            playsound(file_name)


if __name__ == "__main__":
    run_quickstart()
