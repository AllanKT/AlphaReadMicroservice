import speech_recognition as sr
from pydub import AudioSegment
import base64


class AudioToText(object):
	def __init__(self):
		self.r = sr.Recognizer()

	def conversor_3gp_to_wav(self):
		AudioSegment.from_file("audio.3gp").export("audio.wav", format="wav")

	def trascript(self):
		with sr.AudioFile('audio.wav') as source:
			audio = self.r.record(source)
		return self.r.recognize_google(audio, language="pt")

	def save_base64(self, audio_base64):
		with open('audio.3gp', 'wb') as file:
			file.write(base64.b64decode(audio_base64))

	def encode_base64(self, file):
		return base64.encodestring(open(file,"rb").read())