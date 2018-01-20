import speech_recognition as sr
import pyaudio
import wave
from google.cloud import language
from google.cloud import language_v1beta2
import six
from google.cloud.language_v1beta2 import enums

#from google.cloud.language_v1 import types
from google.cloud.language_v1beta2 import types
from google.cloud import language_v1
#from google.cloud.language import types

import wikipediaapi as wk

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Shumpu/Downloads/google/My Project-455e0b88df87.json"

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
    for category in result.categories:
        print('category name: ', category.name)
        print('category confidence: ', category.confidence, '\n')


r = sr.Recognizer()

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 15
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

with sr.AudioFile(audio) as source:
    print("Say")
  #  audio = r.listen(source, phrase_time_limit=10)
    audio = r.record(source)
    print('done')

try:

    asdf = r.recognize_google(audio)
    print("google thinks you said: \n" + asdf)

    classi(asdf)

except:
    print('failed')



'''

def classify_text(text):
    """Classifies content categories of the provided text."""
    print('1')
    client = language_v1.LanguageServiceClient(credentials="AIzaSyD3g1LoWHLAzpZ44phjhuSHGbi-ng1A7NQ")
    print('2')

    if isinstance(text, six.binary_type):
        print('3')
        text = text.decode('utf-8', 'strict')
        print('3.5')


    print('4')
    document = language_v1.types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    print('5')
    categories = client.classify_text(document).categories

    print('6')
    for category in categories:
        print(u'=' * 20)
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))

'''
'''
def classify(text, verbose=True):
    """Classify the input text into categories. """

    print('1')

    language_client = language_v1.LanguageServiceClient(credentials='AIzaSyD3g1LoWHLAzpZ44phjhuSHGbi-ng1A7NQ')

    print('2')

    document = language_v1.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document)
    categories = response.categories

    print('3')
    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u'=' * 20)
            print(u'{:<16}: {}'.format('category', category.name))
            print(u'{:<16}: {}'.format('confidence', category.confidence))

    return result

'''