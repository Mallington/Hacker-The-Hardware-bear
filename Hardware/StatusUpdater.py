import requests
import time
from RobotMoves import Moves
URL = "http://192.168.43.187:8080/DanceMove"
delay = 1



while True:
	data = None
	try:
		r = requests.get(URL)
		data = r.json()
	except Exception as e:
			print("No server connection")

	if(data!= None):
		if data == "Dance":
			print("Dancing!")
			move = Moves()
			move.dance(3)
			move.clear()
		elif data == "Wave":
			print("Waving")
		elif data == "Cuddle":
			print("Cuddling")
	

	time.sleep(delay)
	