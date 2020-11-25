import numpy as np
import matplotlib.pyplot as plt
from MicrophoneStream import MicrophoneStream

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


def plot_audio(audio_gen):
    full_frame = []
    for i, x in enumerate(audio_gen):
        # x=np.fromstring(x, np.int16)
        full_frame.append(x)
        wav = np.frombuffer(x, np.int16)
        plt.cla()
        plt.axis([0, CHUNK * 10, -5000, 5000])
        try:
            plt.plot(wav[-CHUNK * 10:])
        except ValueError:
            plt.plot(wav)
        plt.xlim([0, 2000])
        plt.pause(0.01)


def main():
    plt.ion()
    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        plot_audio(audio_generator)


if __name__ == '__main__':
    main()
    print("end main")
