import sys
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
        plt.plot(wav[-CHUNK * 10:])
        plt.xlim([0, 1500])
        plt.pause(0.01)
        plt.show()


def main():
    plt.ion()
    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        plot_audio(audio_generator)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("end main")
        sys.exit(0)
