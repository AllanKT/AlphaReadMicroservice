from flask import Flask, jsonify, request
from app.audio_transcript import AudioToText
from app.image_recognition import ImageRecognition
import base64
from app import app

@app.route('/audio_to_text', methods = ['POST'])
def audio_to_text():
	try:
		data = request.get_json()
	except:
		return jsonify({'data': 'Request body is invalid. Please send the fields correctly in String format'})

	try:
		audio = AudioToText()
		audio.save_base64(data['data'])
		audio.conversor_3gp_to_wav()
	except Exception as e:
		return jsonify({'data': 'Failed to receive file'})

	try:
		response = audio.trascript()
		print(response)
		return jsonify({'data': response.capitalize()})
	except Exception as e:
		return jsonify({'data': 'Não compreendi o que você falou. Se esforce na próxima!'})

@app.route('/image', methods=['POST'])
def image():
	try:
		user = request.get_json()
	except:
		return jsonify({'data': 'Request body is invalid. Please send the fields correctly in String format'})
	

	try:
		image = ImageRecognition()
		response = image.setImage(user['data'])
		object = image.classifier()
		print(image.getObjeto(object[0][0]))
		return jsonify({'data': image.getObjeto(object[0][0])})
	except:
		return jsonify({'data': 'Is necessary the fields \'data\' in format base64'})