#james muir
#this program simulates breeding with dominant and recessive genes

import random

population = [("d","r"),("d","r"),("d","r"),("d","r"),("d","r"),("d","r"),("d","r"),("d","r")]

def breed_population(pop,numKids):
	new_pop = []
	for i in range(int(len(pop)/2)): #loops the initial length of pop/2
		m = pop.pop(random.randint(0,len(pop)-1))
		d = pop.pop(random.randint(0,len(pop)-1))
		kids = []
		for i in range(numKids):
			kids.append((m[random.randint(0,1)],d[random.randint(0,1)]))
		new_pop.extend(kids)
	return new_pop

def cull_recessive_phenotype(population,chance): #chance is a decimal representing the likelyhood that an individual will be culled if they express the recessive phenotype
	new_pop = []
	for i in population:
		if i[0]==i[1]=="r":
			if random.random()>chance:
				new_pop.append(i)
		else:
			new_pop.append(i)
	return new_pop

#tests
for i in range(1000):
	population = breed_population(population,2)
	population = cull_recessive_phenotype(population,1.0)
print(population)