#The purpose of Importing these two out of syllabus modules...
#Is to Make the game look good else we dont need these...
import os
import time

import random

M=[['  ']]
Trails=[]
px=0
py=0
x=0
y=0
ax=0
ay=0
apple=False
appleCounts=0

#Tried implementing loading but i think the program doesnt need it...
#print('''                          
#      	  █░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀
#	  █▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█•••''')
#time.sleep(1.5)

def MoveTrail():
	for i in range(len(Trails)-1,0,-1):
		Trails[i][0]=Trails[i-1][0]
		Trails[i][1]=Trails[i-1][1]
	if len(Trails)>0:
		Trails[0][0]=x
		Trails[0][1]=y

def TrailCheck():
	for i in Trails:
		while True:
			try:
				a= M[i[1]]
			except IndexError:
				M.append(['  '])
			else:
				try:
					b=M[i[1]][i[0]]
					break
				except IndexError:
					M[i[1]].append('  ')

def update():
	global apple,appleCounts
	for i in M:
		for j in range(len(i)):
			i[j]=' '
	WorldCheck(x,y)
	
	if apple:
		WorldCheck(ax,ay)
		M[ay][ax]='🍎'
	
	if M[y][x] == '🍎':
		appleCounts+=1
		apple=False
		
		try:
			x1=Trails[-1][0]
			y1=Trails[-1][1]
				
			try:
				x2=Trails[-2][0]
				y2=Trails[-2][1]
				Trails.append([x1+(x1-x2),y1+(y1-y2)])
			except IndexError:
				Trails.append([x1+(x1-x),y1+(y1-y)])
		except IndexError:
			Trails.append([x+(px-ax),y+(py-ay)])
	
	for i in Trails:
		TrailCheck()
		M[i[1]][i[0]]='🟩'	
			
	M[y][x]='🟨'
	
	os.system('clear')
	
	for i in M:
		for j in i:
			print(j,end='')
		print()

def WorldCheck(a,b):
	while True:
		try:
			p=M[b]
		except IndexError:
			M.append(['  '])
		else:
			try:
				q=M[b][a]
				break
			except IndexError:
				M[b].append('  ')

while True:
	
	if x<0:
		x=0
	
	if ax<0:
		ax=0
	
	if ay<0:
		ay=0
	
	if y<0:
		y=0
	if not apple:
		ax=random.randint(0,23)
		ay=random.randint(0,20)
		apple=True
	
	update()
	
	dir=int(input('\n\n\n'+str(px)+','+str(py)+' | '+str(x)+','+str(y)+str(Trails)+'\nApple Count:'+str(appleCounts)+'\nEnter 1 for up, 2 for right, 3 for down and 4 for left: '))
	steps=int(input('Enter no. of steps you want to take: '))
	
	if dir == 1:
		for i in range(steps):
			MoveTrail()
			py=y
			px=x
			y-=1
			update()
			time.sleep(0.2)
	elif dir==2:
		for i in range(steps):
			MoveTrail()
			px=x
			py=y
			x+=1
			update()
			time.sleep(0.2)
	elif dir==3:
		for i in range(steps):
			MoveTrail()
			py=y
			px=x
			y+=1
			update()
			time.sleep(0.2)
	elif dir==4:
		for i in range(steps):
			MoveTrail()
			px=x
			py=y
			x-=1
			update()
			time.sleep(0.2)
	else:
		print('invalid Input...')