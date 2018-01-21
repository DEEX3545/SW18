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
   # print('1')
    language_client = language_v1beta2.LanguageServiceClient()

   # print('2')
    document = types.Document(content=text, type = enums.Document.Type.PLAIN_TEXT)
   # print('3')

    result = language_client.classify_text(document)
   # print(4)


    ffa = result.categories

    #print(ffa)

    ar = ['', '']


    counter = 0
    for category in ffa:

        ar[0] = category.name
        ar[1] = category.confidence
       # print(ar)
        break


    return ar


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


def cleanstring(s):

    a = 0
    b = s
    for f in range(len(b)):
        if b[f] == '/':
            b.replace('/', '')

    #b.replace('/', '')
    return b



#----------------------------------------------------

print("Hello, you are using DeStract. To begin, please enter the category you are about to discuss: ")
topic = input("Topic: ")





listening = True

while(on):



    while(listening):

        try:

            toParse = ''

            print(cleanstring('/Science'))
            bee = classi("Chemistry is often called the central science because it deals with elements in both Physics and in Biology. Due to this, chemistry is often a hard subject to study and deal with. One of the reasons is that there is so much memorization and sometimes so much math involved, even calculus.")

            print('category name: ', bee[0])
            print('category confidence: ', bee[1], '\n')

            for f in range(3):
                audio = record()

                with sr.AudioFile(audio) as source:

                    print("-O-")
                    audio = r.record(source)
                    print('-_-')
                asdf = r.recognize_google(audio)
                toParse += asdf

            # bee = classi(toParse)


            #asdf = r.recognize_google(audio)

            print("google thinks you said: \n" + toParse)

            classi(toParse)


        except:

            print('failed')


        finally:

            on = True
