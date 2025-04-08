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

models = np.genfromtxt('data/mtcars.csv', delimiter=',', skip_header=1, dtype=str, usecols=0)

mean_hp = np.mean(hp)
print(f"media de potencia de los coches: {mean_hp}")

# calcula el indice peso/potencia de los coches

power_to_weight = wt / hp
print(f"indice peso/potencia de los coches: {power_to_weight}")

# sacar el coche mas potente

max_hp = np.max(hp)
max_hp_index = np.argmax(hp)
print(f"coche mas potente: {models[max_hp_index]} con {max_hp} hp")

# el que menos eficiencia de combustible 

min_mpg = np.min(mpg)
min_mpg_index = np.argmin(mpg)
print(f"coche menos eficiente: {models[min_mpg_index]} con {min_mpg} mpg")

# son en promedio más potentes los coches con motores en V o en línea?

# filter data for V engines (V=0)

v_engines = data[vs == 0]
v_hp = v_engines[:, 4]

# filter data for straight engines (V=1)
straight_engines = data[vs == 1]
straight_hp = straight_engines[:, 4]

mean_v_hp = np.mean(v_hp)
median_v_hp = np.median(v_hp)
mean_straight_hp = np.mean(straight_hp)
median_straight_hp = np.median(straight_hp)

print(f"media de potencia de los coches V: {mean_v_hp} con mediana {median_v_hp}")
print(f"media de potencia de los coches en linea: {mean_straight_hp} con mediana {median_straight_hp}")

