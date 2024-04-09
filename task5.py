#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days

question = "what is the population?"
p = input(question)
p = float(p)

question = "what is the rate of growth?"
r = input(question)
r = float(r)

question = "what is the numbers of day?"
d = input(question)
d = float(d)

t = d/365

f= p*(1+r)**t 
f= round(f,2)

print(f"what is the future population?{f}")
