import random as r
import os
while True:
	wp=[' ',' ',' ']
	rw=r.choice(['rat','bat','cat','mud','hut','raw','rod'])
	while True:
		os.system('clear')
		gw = input('|'+wp[0]+'|'+wp[1]+'|'+wp[2]+'|'+'\nEnter a 3 digit word to guess: ')
		if gw== rw:
			print('You have guessed it!!')
			break
		else:
			Bad=True
			for i in range(3):
				if gw[i]==rw[i]:
					wp[i]=gw[i]
					input((gw[i]+' ')+ 'is in right position.Press Enter to Continue...')
					Bad=False
				elif gw[i] in rw:
					input(gw[i]+' '+'is not in right position.Press Enter to continue...')
					Bad=False
				else:
					if Bad and i==2:
						input('Bad Guess!! Press Enter to continue...')
	c=int(input('Enter 1 to play again or 0 to exit: '))
	if c==1:
		continue
	else:
		print('Exiting Game...')
		break		
	
