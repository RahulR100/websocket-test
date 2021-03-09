import json, requests, websockets, random, time, asyncio

url = 'wss://nospy-relay.herokuapp.com/ws/'

async def hello(uri):
	async with websockets.connect(uri) as websocket:
		while True:
			await asyncio.sleep(3)
			randval = random.randint(1, 100)
			await websocket.send(
				json.dumps(
					{'value': randval}
				)
			)
			print(randval)

		#await websocket.recv() // we dont receive anything yet

loop = asyncio.get_event_loop()
try:
	asyncio.ensure_future(hello(url))
	loop.run_forever()
except KeyboardInterrupt:
	pass
finally:
	print("Closing Loop")
	loop.close()