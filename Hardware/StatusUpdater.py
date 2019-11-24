import requests
import time
from RobotMoves import Moves
URL = "http://192.168.43.187:8080/DanceMove"
delay = 1

move = Moves()
move.clear()
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
			move.dance(2)
			move.clear()
		elif data == "Wave":
			print("Waving")
			move.wave(1)
			move.clear()
		elif data == "Cuddle":
			move.cuddle(1)
			move.clear()
			print("Cuddling")
	

	time.sleep(delay)
	
