from qhue import Bridge, create_new_username
import time
import numpy as np
import lightfunctions as lf

# blink and change colours, lasts 20 secs
def blinkcolourchange(b,order):
	for i in range(10):
		lf.colour(b, lf.goodcolour(), order)
		lf.blink(b,2,0.49)

def peakshow(b,order):

	lf.oncolours(b,order)

	for i in range(3):
		lf.alternate2crb(b,20,3,False)

	lf.colourwaves(b,order,25,5,30000)
	lf.colourwaves(b,order[::-1],25,5,30000)

	lf.sweepbackforth(b,40,False)

	lf.alternate2crb(b,40,1,True)
	
	blinkcolourchange(b,order)

	for i in range(3):		
		lf.alternate2cr(b,20,0.75,False)
		lf.alternate2crb(b,40,0.5,True)


	lf.sweepbackforth(b,60,True)

if __name__ == "__main__":

	lights = [3,0,1,2]

	bridge_IP = '192.168.1.100'
	"""
	username = None

	if username is None:
		username = create_new_username(bridge_IP)
		print("New user: {} . Put this in the username variable above (line 41).".format(username))
	"""
	username = 'fGx1IUPbQu39QzOwdsAxRjl9tnLMYnySuu5PBCXZ'

	b = Bridge(bridge_IP,username)

	# initial slow loop for first 2.5hrs
	# in units of seconds
	part1_duration = 60

	start = time.time()
	while part1_duration > time.time() - start:
		print('Colour alternate')
		lf.colouralternate(b,60,1)
		print('Colour waves')
		lf.colourwaves(b,lights,60,30,30000)
		print('part 1 continue')

	print('part 2')
	start = time.time()
	while 60 > time.time() - start:	
		start2 = time.time()
		while 60 > time.time() - start2:
			print('peak show')
			peakshow(b,lights)
		print('Colour alternate')
		lf.colouralternate(b,60,1)
		print('Colour waves')
		lf.colourwaves(b,lights,60,30,30000)
		print('part 2 continue')

	
	print('part 3')
	start = time.time()
	while 60 > time.time() - start:
		print('Colour alternate')
		lf.colouralternate(b,60,1)
		print('Colour waves')
		lf.colourwaves(b,lights,60,30,30000)
		print('part 3 continue')

