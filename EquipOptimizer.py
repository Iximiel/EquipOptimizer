#EquipOptimizer using Montecarlo for fun, can be used for anything, i think
#Maybe this is not the best thing on the net
#@Author: Daniele Rapetti
#@email: iximiel@gmail.com
#@version:0.1
#Enjoy
from random import randint, uniform
from math import exp

f=open("Settings.in",'r')
line=f.readline()
line=line.partition('#')[0]
while not line:
	line=f.readline()
	line=line.partition('#')[0]
Nstat=int(line)
Stats=[]
Weight=[]
print "Number of stat to analyze: " + str(Nstat)
n=0
while n <Nstat:
	line=f.readline()
	line = line.partition('#')[0]
	line = line.rstrip()
	if line:
		data = line.split()
		Stats.append(data[0])
		Weight.append(float(data[1]))
		n+=1
		
for n in range(0,Nstat):
	print "*\t"+Stats[n]+"\tweight= "+str(Weight[n])

line=f.readline()
line=line.partition('#')[0]
while not line:
	line=f.readline()
	line=line.partition('#')[0]
Nequips = int(line)
print "Files with the equipments:"
n=0
EquipFiles=[]
while n <Nequips:
	line=f.readline()
	line = line.partition('#')[0]
	line = line.rstrip()
	if line:
		EquipFiles.append(line)
		n+=1
		
		
for n in range(0,Nequips):
	print "*\t"+EquipFiles[n]
	
line=f.readline()
line=line.partition('#')[0]
while not line:
	line=f.readline()
	line=line.partition('#')[0]
MC_T=float(line)

line=f.readline()
line=line.partition('#')[0]
while not line:
	line=f.readline()
	line=line.partition('#')[0]
Nsteps=int(line)
f.close()
print "Temperature: "+str(MC_T)
print "Steps: "+str(Nsteps)

Equips=[]
EquipRanges=[]
#reading the equips files:
for ef in EquipFiles:
	tdata=[]
	with open(ef,'r') as f:
		for line in f:
			line = line.split('#', 1)[0]
			line = line.rstrip()
			if line:
				data = line.split()
				tdata.append(data)
	EquipRanges.append(len(tdata)-1)
	Equips.append(tdata)
'''
for n in range(0,Nequips):
	print "*\t"+EquipFiles[n]
	print EquipRanges[n]
	print Equips[n]
'''
#this is the "last accepted step"
OldEnergy=0.0
OldCombination=[]
for neq in range(0,Nequips):
	tdata=Equips[neq]
	rnd=randint(0,EquipRanges[neq])
	OldCombination.append(rnd)
	for n in range(1,Nstat+1):
		OldEnergy+=float(tdata[rnd][n])*Weight[n-1]
                
#saving the best combination
bestStep=0
BestEnergy=OldEnergy
BestCombination=OldCombination
print "Starting equipment strenght: "+str(OldEnergy)
step=0
while step<=Nsteps:
	NewCombination = OldCombination
	#select a type of gear
	rndtype = randint(0,Nequips-1)
	NewCombination[rndtype] = randint(0,EquipRanges[rndtype])
	NewE=0.0
	for neq in range(0,Nequips):
		tdata=Equips[neq]
		for n in range(1,Nstat+1):
			NewE+=float(tdata[NewCombination[neq]][n])*Weight[n-1]
	#montecarlo happens here:
	#Delta is inverted because we are maximizing the Energy
	deltaE = OldEnergy-NewE
	expAcc = exp(-deltaE/MC_T)
	z = uniform(0.0,1.0)
	if z < expAcc:
		OldCombination = NewCombination
		OldEnergy = NewE
                if OldEnergy > BestEnergy:
                        #saving the best combination
                        BestEnergy=OldEnergy
                        BestCombination=OldCombination
                        bestStep=step

	step+=1

print "Final equipment strenght: "+str(BestEnergy)
print "Found a best combination:"
for neq in range(0,Nequips):
	tdata=Equips[neq]
	print tdata[BestCombination[neq]]
        
print "Found at step " +str(bestStep)
print "Run me another couple of times to see if it is really the best, try changing the \"temperature\""
