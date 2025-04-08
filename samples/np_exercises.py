import numpy as np
# open mtcars.csv
data = np.genfromtxt('data/mtcars.csv', delimiter=',', skip_header=1)

""""
mpg - Miles per Gallon
cyl - number of cylinders
disp - displacement, in cubic inches, which is the volume of the engine
hp - horsepower
drat - driveshaft ratio, which is how fast the driveshaft is turning compared to the engine
wt - weight
qsec - 1/4 mile time; a measure of acceleration
vs - 'V' or straight - engine shape
am - transmission; auto or manual
gear - number of forward gears
carb - number of carburetors
"""

mpg = data[:, 1]  # mpg
cyl = data[:, 2]  # cyl
disp = data[:, 3]  # disp
hp = data[:, 4]  # hp
drat = data[:, 5]  # drat
wt = data[:, 6]  # wt
qsec = data[:, 7]  # qsec
vs = data[:, 8]  # vs
am = data[:, 9]  # am
gear = data[:, 10]  # gear
carb = data[:, 11]  # carb

# get model name from original file as a list of strings 

models = np.genfromtxt('data/mtcars.csv', delimiter=',', skip_header=1, dtype=str, usecols=0)

mean_hp = np.mean(hp)
print(f"media de potencia de los coches: {mean_hp}")

# calcula el indice peso/potencia de los coches

power_to_weight = hp / wt
print(f"indice peso/potencia de los coches: {power_to_weight}")

# sacar el coche mas potente

max_hp = np.max(hp)
max_hp_index = np.argmax(hp)
print(f"coche mas potente: {data[max_hp_index, 0]} con potencia {max_hp}")

# el que menos eficiencia de combustible 

# son en promedio más potentes los coches con motores en V o en línea?

