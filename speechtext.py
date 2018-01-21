import speech_recognition as sr
import pyaudio
import wave


from google.cloud import language_v1beta2
from google.cloud.language_v1beta2 import enums
from google.cloud.language_v1beta2 import types

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Shumpu/Downloads/google/My Project-455e0b88df87.json"

on = True

#'''credentials="AIzaSyD3g1LoWHLAzpZ44phjhuSHGbi-ng1A7NQ"'''
#AIzaSyD3g1LoWHLAzpZ44phjhuSHGbi-ng1A7NQ
#credentials="AIzaSyC0ueTFpiKw40rXgZaWJyle_dW_t3sddnU"
def classi(text):
    print('1')
    language_client = language_v1beta2.LanguageServiceClient()

    print('2')
    document = types.Document(content=text, type = enums.Document.Type.PLAIN_TEXT)
    print('3')

    result = language_client.classify_text(document)
    print(4)

    return result.categories


r = sr.Recognizer()

def record():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "C:/Users/Shumpu/PycharmProjects/machine learning/tensorlfowstuff/audio.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
     data = stream.read(CHUNK)
     frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


    audio = 'audio.wav'
    return audio






#----------------------------------------------------

print("Hello, you are using DeStract. To begin, please enter the category you are about to discuss: ")
topic = input("Topic: ")







while(on):


    audio = record()

    with sr.AudioFile(audio) as source:

        print("Say")
        audio = r.record(source)
        print('done')

    try:

        asdf = r.recognize_google(audio)
        print("google thinks you said: \n" + asdf)

        ffa = classi(asdf)

        for category in ffa:
            print('category name: ', category.name)
            print('category confidence: ', category.confidence, '\n')

    except:

        print('failed')


    finally:

        on = True
