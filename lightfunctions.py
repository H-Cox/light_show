from qhue import Bridge
import time
import numpy as np

# select a random brightness
def rbrightness():

	return np.random.randint(0,256)

# select a random light
def rlight(number_lights):

	return np.random.randint(1,number_lights+1)

# select a random colour
def rcolour():

	return np.random.randint(0,65536)

# select a simple random colour
def rscolour():

	return 2500*np.random.randint(0,27)

# select a really simple colour
def rsscolour():

	return 10000*np.random.randint(0,7)

def goodcolour():

	colours = [0,5000,10000,18000,24000,43000,46000,48000,51000,54000,59000]

	return colours[np.random.randint(0,11)]

# turn all the lights on
def allon(b):
	for i in range(len(b.lights())):

		b.lights(i+1,'state',on=True)

# turn all the lights off
def alloff(b):

	for i in range(len(b.lights())):

		b.lights(i+1,'state',on=False)

# set all lights to saturation 255
def maxsat(b):
	
	for i in range(len(b.lights())):

		b.lights(i+1, 'state', sat = 255)

# set lights in list 'lights' to saturation sat
def sat(b,sat,lights):

	for i in lights:

		b.lights(i+1, 'state', sat = sat)

# set lights in list 'lights' to brightness bri
def bright(b, brightness, lights):

	for i in lights:

		b.lights(i+1,'state',bri=brightness, transitiontime = 1)

# set lights in list 'lights' to colour hue
def colour(b, hue, lights):
	for i in lights:

		b.lights(i+1,'state', hue = hue)

# set lights in list 'lights' to colour hue and brightness bri
def cb(b,hue,brightness,lights):
	
	for i in lights:

		b.lights(i+1,'state', hue = hue, bri = brightness)

# turn on lights in list 'lights'
def on(b, lights):

	for i in lights:
		b.lights(i+1,'state', on = True)

# turn off light in list 'lights'
def off(b,lights):

	for i in lights:
		b.lights(i+1,'state', on = False)

# alternate half the lights on and off
def alternate2(b,duration,wait):
	# duration is overall running time of script
	# wait is time each pair spends on or off

	# find number of lights and set transition time
	n = len(b.lights())
	tt = 0
	
	# randomise order
	li = np.random.permutation(range(n))

	# calculate half or round down to half
	split = int(n/2)

	# determine two groups of lights
	g1 = li[:split]
	g2 = li[split:]

	# initiate loop until time is up
	state = True
	start = time.time()
	while duration > time.time() - start:
		# switch on or off depending on state
		if state:
			# turn on group 1
			for i in g1:
				b.lights(i+1,'state', on = True, transitiontime = tt)
			# turn off group 2
			for i in g2:
				b.lights(i+1,'state', on = False, transitiontime = tt)
			# switch state
			state = False	
		else:
			# turn on group 2
			for i in g2:
				b.lights(i+1,'state', on = True, transitiontime = tt)
			# turn off group 1
			for i in g1:
				b.lights(i+1,'state', on = False, transitiontime = tt)
			# switch state
			state = True
		# wait
		time.sleep(wait)

# alternate half the lights on and off with random colours
def alternate2crb(b,duration,wait,colourmix):
	# duration is overall running time of script
	# wait is time each pair spends on or off

	# find number of lights and set transition time
	n = len(b.lights())
	tt = 1

	# randomise order
	li = np.random.permutation(range(n))

	# calculate half or round down to half
	split = int(n/2)

	# determine two groups of lights
	g1 = li[:split]
	g2 = li[split:]

	allon(b)
	# initiate loop until time is up
	state = True
	start = time.time()
	while duration > time.time() - start:

		# switch on or off depending on state
		if state:
			# turn off group 2
			for i in g2:
				b.lights(i+1,'state', bri = 0 , transitiontime = tt)
			# turn on group 1 and select random colour
			c1 = goodcolour()
			for i in g1:
				if colourmix:
					c1 = goodcolour()
				b.lights(i+1,'state', bri = 100, hue = c1, transitiontime = tt)
			# switch state
			state = False	
		else:
			# turn off group 1
			for i in g1:
				b.lights(i+1,'state', bri = 0, transitiontime = tt)
			# turn on group 2 and select random colour
			c2 = goodcolour()
			for i in g2:
				if colourmix:
					c2 = goodcolour()
				b.lights(i+1,'state', bri = 100, hue = c2, transitiontime = tt)
			# switch state
			state = True
		# wait
		time.sleep(wait)

# alternate half the lights on and off with random colours
def alternate2cr(b,duration,wait,colourmix):
	# duration is overall running time of script
	# wait is time each pair spends on or off

	# find number of lights and set transition time
	n = len(b.lights())
	tt = 1

	# randomise order
	li = np.random.permutation(range(n))

	# calculate half or round down to half
	split = int(n/2)

	# determine two groups of lights
	g1 = li[:split]
	g2 = li[split:]

	# initiate loop until time is up
	state = True
	start = time.time()
	while duration > time.time() - start:

		# switch on or off depending on state
		if state:
						# turn off group 2
			for i in g2:
				b.lights(i+1,'state', on = False, transitiontime = tt)
			# turn on group 1 and select random colour
			c1 = goodcolour()
			for i in g1:
				if colourmix:
					c1 = goodcolour()
				b.lights(i+1,'state', on = True, hue = c1, transitiontime = tt)

			# switch state
			state = False	
		else:
			# turn off group 1
			for i in g1:
				b.lights(i+1,'state', on = False, transitiontime = tt)
			# turn on group 2 and select random colour
			c2 = goodcolour()
			for i in g2:
				if colourmix:
					c2 = goodcolour()
				b.lights(i+1,'state', on = True, hue = c2, transitiontime = tt)
			# switch state
			state = True
		# wait
		time.sleep(wait)

# blink all lights
def blink(b,duration,wait):
	# duration is overall running time of script
	# wait is time lights spend on or off
	n = list(range(len(b.lights())))
	# start timer and turn lights on at max brightness
	start = time.time()
	state = True
	allon(b)
	bright(b,100,n)

	# loop blinking lights
	while duration > time.time() - start:
		# wait
		time.sleep(wait)
		# determine what to do
		if state:
			# turn down brightness
			bright(b,0,n)
			# change state
			state = False
		else:
			# turn up brightness
			bright(b,100,n)
			# change state
			state = True


# strobe all lights
def strobe(b,duration,wait):
	# duration is overall running time of script
	# wait is time lights spend on or off
	n = list(range(len(b.lights())))
	# start timer and turn lights on at max brightness
	start = time.time()
	state = True
	allon(b)
	bright(b,255,n)
	# loop blinking lights
	while duration > time.time() - start:
		# wait
		time.sleep(wait)
		# determine what to do
		if state:
			# turn down brightness
			alloff(b)
			# change state
			state = False
		else:
			# turn up brightness
			allon(b)
			# change state
			state = True


def sweepon(b,lights,wait):

	for i in lights:
		b.lights(i+1,'state', on = True, transitiontime = 1)
		time.sleep(wait)

def sweeponc(b,lights,wait):
	c = goodcolour()
	for i in lights:
		b.lights(i+1,'state', on = True, hue = c, bri = 50, transitiontime = 1)
		time.sleep(wait)

def sweepoff(b,lights,wait):

	for i in lights:
		b.lights(i+1,'state', on = False, transitiontime = 1)
		time.sleep(wait)

# script which alternates lights between brightnesses and colours
def colouralternate(b,duration,wait):
	# hue values to use
	colours = [0,5000,10000,18000,24000,43000,46000,48000,51000,54000,59000]

	# number of lights
	n = len(b.lights())
	
	# set transition time
	tt = 8

	# set min and max brightnesses
	maxbri = 50
	minbri = 0

	# turn all lights on and set max saturation and brightness
	for i in range(n):
		b.lights(i+1,'state', on = True, hue = goodcolour(), bri = maxbri, sat = 255)

	# turn on timer and loop until time is up
	start = time.time()
	while duration > time.time()-start:
		# randomly pick a higher brightness
		if np.random.randint(1,30) == 9:
			maxbri2 = 100
		else:
			maxbri2 = maxbri

		for i in np.random.permutation(range(n)):
			# change settings of each light to a random colour
			b.lights(i+1,'state',hue = colours[np.random.randint(0,11)],bri = np.random.randint(minbri,maxbri2), transitiontime = tt)
			time.sleep(wait)

# alternate lights with varying wait times and sweeps between
def colouraltsweep(b,maxwait,minwait,altd,runs,light_order):
	# inputs are b, max and minimum waiting time for alternation,
	# alternation durations, and number of downwards/upward runs
	print("Starting colour-alt-sweep...")

	# find number of lights
	n = len(b.lights())

	# calculate waiting times and set waiting order
	wait = np.linspace(maxwait,minwait,runs)
	order = np.concatenate((wait,wait[1::-1]))

	# estimate overall time to completion
	tcomp = (2*altd+1+4+1)*len(order)
	print("Estimated to finish in {0} secs".format(tcomp))

	# loop through all the waiting times
	for t,j in enumerate(order):
		print('Iteration {0}, of {1}'.format(t,len(order)))

		# Main alternating lights part
		alternate2cr(b,altd,j)
		alternate2cr(b,altd,j)

		# turn off lights and wait
		for i in range(n):
			b.lights(i+1,'state',on=False, transitiontime = 5)
		time.sleep(1)

		# turn on lights with a sweep and wait
		if t < int(len(order)/2):
			sweeponc(b,light_order,1)
		else:
			sweeponc(b,light_order[::-1],1)
		time.sleep(1)

def oncolours(b, light_order):
	# set the colours to be used (max 8)
	colours = [0,5000,10000,18000,24000,43000,51000,54000]

	# all the lights should be off
	alloff(b)

	# turn on in a sweep and wait
	for i in light_order:
		b.lights(i+1,'state', on = True, hue = 24000, transitiontime = 8)
		time.sleep(1)
	time.sleep(1)

	# turn off in a sweep and wait
	for i in light_order:
		b.lights(i+1,'state', on = False, transitiontime = 8)
		time.sleep(1)

	# loop through the colours blinking on and off
	for n,c in enumerate(colours):
		# on
		for i in light_order:
			b.lights(i+1,'state', on = True, hue = c, transitiontime = (8))
		time.sleep(1)
		# off
		for i in light_order:
			b.lights(i+1,'state', on = False, transitiontime = (8))
		time.sleep(1)

def oncolours2(b, light_order):
	# set the colours to be used (max 8)
	colours = [0,5000,10000,18000,24000,43000,51000,54000]

	# all the lights should be off
	alloff(b)

	# loop through the colours blinking on and off
	for n,c in enumerate(colours):
		# on
		for i in light_order:
			b.lights(i+1,'state', on = True, hue = c, transitiontime = (8))
		time.sleep(0.5)
		# off
		for i in light_order:
			b.lights(i+1,'state', on = False, transitiontime = (8))
		time.sleep(0.5)

def sweepbackforth(b,duration,onoff):
	allon(b)
	start = time.time()
	while duration > time.time()-start:
		if onoff:
			for j in range(4):
				b.lights(j+1,'state',on=False, transitiontime = 1)
		time.sleep(0.5)
		sweeponc(b,[3,0,1,2],0.25)
		if onoff:
			for j in range(4):
				b.lights(j+1,'state',on=False, transitiontime = 1)
		time.sleep(0.5)
		sweeponc(b,[2,1,0,3],0.25)

# 
def colourwaves(b,lights,duration,period,huespace):
	allon(b)

	huestep = 63000/(period*2)
	hueset = np.linspace(0,huespace,5)
	hueset = hueset[:4]

	for i,l in enumerate(lights):
		hl = list(hueset)
		b.lights(int(l+1),'state',on=True,bri=75,hue = int(hl[i]), sat=255)

	start = time.time()
	while duration > time.time() - start:
		hl = list(hueset)
		for i,l in enumerate(lights):
			b.lights(int(l+1),'state',hue = int(hl[i]),transitiontime = 5)
		
		hueset = hueset + huestep

		hueset[hueset > 63000] = hueset[hueset > 63000] - 63000
		time.sleep(0.5)

		
		

















