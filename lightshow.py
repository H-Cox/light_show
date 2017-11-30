from qhue import Bridge
import time
import numpy as np
import lightfunctions as lf

# blink and change colours, lasts 20 secs
def blinkcolourchange(b):
	for i in range(10):
		lf.colour(b, lf.goodcolour(), [3,0,1,2])
		lf.blink(b,2,0.49)

def peakshow(b):

	lf.oncolours(b)

	for i in range(3):
		lf.alternate2crb(b,20,3,False)

	lf.colourwaves(b,[3,0,1,2],25,5,30000)
	lf.colourwaves(b,[2,1,0,3],25,5,30000)

	lf.sweepbackforth(b,40,False)

	lf.alternate2crb(b,40,1,True)
	
	blinkcolourchange(b)

	for i in range(3):		
		lf.alternate2cr(b,20,0.75,False)
		lf.alternate2crb(b,40,0.5,True)


	lf.sweepbackforth(b,60,True)

maxwait = 2
minwait = 0.5
altd = 3
runs = 3
lights = [3,0,1,2]
duration = 20
period = 4.9

b = Bridge('192.168.1.100', 'fGx1IUPbQu39QzOwdsAxRjl9tnLMYnySuu5PBCXZ')

# initial slow loop for first 2.5hrs

start = time.time()
while 60*20 > time.time() - start:
	print('Colour alternate')
	lf.colouralternate(b,60*10,1)
	print('Colour waves')
	lf.colourwaves(b,[3,0,1,2],60*5,30,30000)
	print('part 1 continue')

print('part 2')
start = time.time()
while 60*20 > time.time() - start:	
	start2 = time.time()
	while 10*60 > time.time() - start2:
		print('peak show')
		peakshow(b)
	print('Colour alternate')
	lf.colouralternate(b,60*5,1)
	print('Colour waves')
	lf.colourwaves(b,[3,0,1,2],60*5,30,30000)
	print('part 2 continue')

	
print('part 3')
start = time.time()
while 60*300 > time.time() - start:
	print('Colour alternate')
	lf.colouralternate(b,60*10,1)
	print('Colour waves')
	lf.colourwaves(b,[3,0,1,2],60*5,30,30000)
	print('part 3 continue')