import random as r
import os
import time

M=[['  ']]
Boxes=[]
Mb=''
score=0
GameOver=False

def SpawnBlock(type):
	global Mb
	x=r.randint(0,14)
	Boxes.append([])
	block=r.choice(['🟥','🟨','🟩','🟦'])
	if type==1:
		Boxes[-1].append([x,0,block])
		Boxes[-1].append([x,1,block])
		Boxes[-1].append([x,2,block])
		Boxes[-1].append([x,3,block])
	elif type==2:
		Boxes[-1].append([x,0,block])
		Boxes[-1].append([x+1,0,block])
		Boxes[-1].append([x,1,block])
		Boxes[-1].append([x+1,1,block])
	elif type ==3:
		Boxes[-1].append([x,0,block])
		Boxes[-1].append([x,1,block])
		Boxes[-1].append([x,2,block])
		Boxes[-1].append([x+1,2,block])
	elif type==4:
		Boxes[-1].append([x,0,block])
		Boxes[-1].append([x+1,0,block])
		Boxes[-1].append([x+2,0,block])
		Boxes[-1].append([x+1,1,block])
	elif type==5:
		Boxes[-1].append([x,0,block])
		Boxes[-1].append([x,1,block])
		Boxes[-1].append([x,2,block])
		Boxes[-1].append([x-1,2,block])
	elif type==6:
		Boxes[-1].append([x,0,block])
		Boxes[-1].append([x,1,block])
		Boxes[-1].append([x-1,1,block])
		Boxes[-1].append([x-1,2,block])
	elif type==7:
		Boxes[-1].append([x,0,block])
		Boxes[-1].append([x,1,block])
		Boxes[-1].append([x+1,1,block])
		Boxes[-1].append([x+1,2,block])
	Mb=Boxes.index(Boxes[-1])

def MoveBlocks():
	global Mb
	BoxMod=Boxes.copy()
	BoxMod.remove(Boxes[Mb])
	GroundUnder=False
	for i in Boxes[Mb]:
		if GroundUnder:
			break
		
		for j in BoxMod:
			try:
				if [i[0],i[1]+1,j[0][2]] in j:
					GroundUnder=True
					break
			except:
				pass
		if i[1]+1>14:
			GroundUnder=True
			break
			
	if not GroundUnder:
		for i in Boxes[Mb]:
			i[1]+=1
	else:
		Mb=''

def WorldCheck(x,y):
	while True:
		try:
			a=M[y]
		except IndexError:
			M.append(['  '])
		else:
			try:
				b=M[y][x]
				break
			except IndexError:
				M[y].append('  ')

def RenderBlocks():
	os.system('clear')
	
	for i in M:
		for j in i:
			i[i.index(j)]='  '
	
	for i in Boxes:
		for j in i:
			WorldCheck(j[0],j[1])
			M[j[1]][j[0]]=j[2]
	
	for i in M:
		for j in i:
			print(j,end='')
		print()

while True:
	if Mb=="":
		a=1
		for index,i in enumerate(M):
			iMod=list(eval(str(i.copy()).replace(", '  '",'')))
			if len(iMod)>=16:
				score+=160*a
				for j in iMod:
					for k in Boxes:
						if [iMod.index(j),index,j] in k:
							k.remove([iMod.index(j),index,j])
							iMod[iMod.index(j)]=' '
							break
				M.remove(i)
				M.insert(index,['  '])
				a+=1
		#Enter direct block no. to get specificly that block every time.Else put a randint range to get randoms.
		SpawnBlock(r.randint(1,7))
	
	for i in Boxes:
		for j in i:
			if Mb != Boxes.index(i) and j[1]==0:
				GameOver = True
	if GameOver:
		break
				
	try:
		for i in Boxes[Mb]:
			if i[0]<0:
				i[0]=0
	except:
		pass
	
	RenderBlocks()
	n=input('\n\n\n'+'\nScore: '+str(score)+'\n1 for left, 2 for right and Enter to move the block downwards: ')
	if n=='1':
		GoodToMove=True
		for i in Boxes[Mb]:
			if not GoodToMove:
				break
			
			if i[0]-1>-1:
				BM = Boxes.copy()
				BM.remove(Boxes[Mb])
				for j in BM:
					try:
						if [i[0]-1,i[1],j[0][2]] in j:
							GoodToMove=False
							break
					except:
						pass
			else:
				GoodToMove=False
				break
		
		if GoodToMove:
				for i in Boxes[Mb]:
					i[0]-=1
		RenderBlocks()
		time.sleep(0.2)
	elif n=='2':
		GoodToMove=True
		for i in Boxes[Mb]:
			if not GoodToMove:
				break
			
			if i[0]+1<16:
				BM = Boxes.copy()
				BM.remove(Boxes[Mb])
				for j in BM:
					try:
						if [i[0]+1,i[1],j[0][2]] in j:
							GoodToMove=False
							break
					except:
						pass
			else:
				GoodToMove=False
				break
		
		if GoodToMove:
				for i in Boxes[Mb]:
					i[0]+=1
		RenderBlocks()
		time.sleep(0.2)
	MoveBlocks()
os.system('clear')
print("Game Over!!!")