#EquipOptimizer using Montecarlo for fun, can be used for anything, i think
#Maybe this is not the best thing on the net
#@Author: Daniele Rapetti
#@email: iximiel@gmail.com
#@version:0.1
#Enjoy

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
		n=n+1
		
for n in range(0,Nstat):
	print "*\t"+Stats[n]+"\tweight= "+str(Weight[n])

line=f.readline()
line=line.partition('#')[0]
while not line:
	line=f.readline()
	line=line.partition('#')[0]
Nfiles = int(line)
print "Files with the equipments:"
n=0
EquipFiles=[]
while n <Nfiles:
	line=f.readline()
	line = line.partition('#')[0]
	line = line.rstrip()
	if line:
		EquipFiles.append(line)
		n=n+1
		
		
for n in range(0,Nfiles):
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

print "Temperature: "+str(MC_T)
print "Steps: "+str(Nsteps)