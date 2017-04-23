# EquipOptimizer
A small utility in python to maximize equipments in simple cases, it has some degrees of versatility
##Usage
- First of all you should edit the file Settings.in:

````
#this is the setting file, you can comment with #
5 #number of stat on the equipment files, write donw the names and their weight
Intellect 0.1
# you can comment everywhere
Critical_Strike 0.5
Haste 0.1
Mastery 0.6
Versatility 1
2# number of equipment files, then name of them
head.in
chest.in
#it's a montecarlo: input the "temeperature"
1
#and the number of "steps"
100000
````
- Then you shold add the files that contains the data of the equipment, please remember a few rules:
  - The data should be written in a table with tsv format with the name of the equipment on the first column and the values of the stat on the other colums, remember to use always the same number of stat as declared in Settings.in
  ````
  name val1 val2 val3 ... val_nstat
  ````
  - Never write a space in the names of the equipment 
  - Remember to write all the values for the stat written in Settings.in, you can use 0 if the stats are absents
 an example:
````
cname1 5 3 0 15 0
cname2 1 0 0 15 0
cname3 0 3 4 13 0
cname4 1 3 4 12 0
````

- After all the set up you can finally launche this utility
- You simply need to lauch the file EquipOptimizer.py with [python 2.7](https://www.python.org/)
