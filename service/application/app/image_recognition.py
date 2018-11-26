import base64
import app.label

class ImageRecognition(object):
	def __init__(self):
		self.objetos = {"arvore": "Árvore", 
						"cadeira": "Cadeira",
						"caderno": "Caderno",
						"carro": "Carro", 
						"casa": "Casa",
						"celular": "Celular",
						"guarda-chuva": "Guarda-chuva",
						"mesa": "Mesa",
						"mochila": "Mochila",
						"monitor": "Monitor",
						"mouse": "Mouse",
						"onibus": "Ônibus",
						"porta": "Porta",
						"teclado": "Teclado"}

	def setImage(self, imageB64):
		with open('image.jpg', 'wb') as file:
			file.write(base64.b64decode(imageB64))
		return 'imagem salva com sucesso'

	def classifier(self):
		return label.execute()

	def getObjeto(self, id = str):
		return self.objetos[id]