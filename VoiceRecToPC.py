import os
import time
import wave
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

#RECORD_SECONDS = 5
#RECORD_SECONDS = 15
RECORD_SECONDS = 30
#RECORD_SECONDS = 60

DEVICE_INDEX = None

#USB_PATH = "D:/CpSound"
USB_PATH = "D/CpSound" #treba dorobiť Priečinok CpSound #

FILENAME_PREFIX = "sound"
FILE_EXTENSION = ".wav"

while True:
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=DEVICE_INDEX,
                    frames_per_buffer=CHUNK)

    frames = []

    print("Recording...")
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    filename = FILENAME_PREFIX + str(int(time.time())) + FILE_EXTENSION
    filepath = os.path.join(USB_PATH, filename)

    wf = wave.open(filepath, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"Saved recording to {filepath}")

    time.sleep(1)
