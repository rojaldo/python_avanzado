# https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv

import pandas as pd

# Cargar el dataset de Titanic

try:
    df = pd.read_csv('data/titanic.csv')
except FileNotFoundError:
    print("No se encontró el archivo 'titanic.csv'. Asegúrate de que está en la carpeta 'data'.")
    exit()
except pd.errors.EmptyDataError:
    print("El archivo 'titanic.csv' está vacío.")
    exit()
except pd.errors.ParserError:
    print("Error al analizar el archivo 'titanic.csv'. Asegúrate de que está bien formado.")
    exit()
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
    exit()
else:
    print("Archivo 'titanic.csv' cargado correctamente.")


# Encontrar numero de pasajeros por clase

passengers_first_class = df[df['pclass'] == 1].shape[0]
passengers_second_class = df[df['pclass'] == 2].shape[0]
passengers_third_class = df[df['pclass'] == 3].shape[0]

print(f"Numero de pasajeros en primera clase: {passengers_first_class}")
print(f"Numero de pasajeros en segunda clase: {passengers_second_class}")
print(f"Numero de pasajeros en tercera clase: {passengers_third_class}")

# numero de supervivientes por clase

survivors_first_class = df[(df['pclass'] == 1) & (df['survived'] == 1)].shape[0]
survivors_second_class = df.query('pclass == 2 and survived == 1').shape[0]
survivors_third_class = df.query('pclass == 3 and survived == 1').shape[0]

print(f"Numero de supervivientes en primera clase: {survivors_first_class}")
print(f"Numero de supervivientes en segunda clase: {survivors_second_class}")
print(f"Numero de supervivientes en tercera clase: {survivors_third_class}")

# probabilidad de supervivencia por clase

survival_rate_first_class = survivors_first_class / passengers_first_class
survival_rate_second_class = survivors_second_class / passengers_second_class
survival_rate_third_class = survivors_third_class / passengers_third_class

print(f"Probabilidad de supervivencia en primera clase: {survival_rate_first_class:.2%}")
print(f"Probabilidad de supervivencia en segunda clase: {survival_rate_second_class:.2%}")
print(f"Probabilidad de supervivencia en tercera clase: {survival_rate_third_class:.2%}")

# probabilidad de supervivencia por sexo

number_of_women = df[(df['sex'] == 'female') ].shape[0]
number_of_men = df[(df['sex'] == 'male') ].shape[0]
number_of_women_survived = df[(df['sex'] == 'female') & (df['survived'] == 1)].shape[0]
number_of_men_survived = df[(df['sex'] == 'male') & (df['survived'] == 1)].shape[0]

print( f'hombres supervivientes: {number_of_men_survived/number_of_men:.2%}')
print( f'mujeres supervivientes: {number_of_women_survived/number_of_women:.2%}')

# media de la edad de los pasajeros

mean_age = df['age'].mean()
print(f"Media de la edad de los pasajeros: {mean_age:.2f}")

# media, mediana y quartiles de la edad de los pasajeros supervivientes

mean_age_survived = df[df['survived'] == 1]['age'].mean()
median_age_survived = df[df['survived'] == 1]['age'].median()
quartiles_age_survived = df[df['survived'] == 1]['age'].quantile([0.25, 0.5, 0.75])
print(f"Media de la edad de los pasajeros supervivientes: {mean_age_survived:.2f}")
print(f"Mediana de la edad de los pasajeros supervivientes: {median_age_survived:.2f}")
print(f"Quartiles de la edad de los pasajeros supervivientes: {quartiles_age_survived.to_dict()}")

# media, mediana y quartiles de la edad de los pasajeros no supervivientes

mean_age_not_survived = df[df['survived'] == 0]['age'].mean()
median_age_not_survived = df[df['survived'] == 0]['age'].median()
quartiles_age_not_survived = df[df['survived'] == 0]['age'].quantile([0.25, 0.5, 0.75])
print(f"Media de la edad de los pasajeros no supervivientes: {mean_age_not_survived:.2f}")
print(f"Mediana de la edad de los pasajeros no supervivientes: {median_age_not_survived:.2f}")
print(f"Quartiles de la edad de los pasajeros no supervivientes: {quartiles_age_not_survived.to_dict()}")

# plot survivors by age

age_not_survived = df[df['survived'] == 0]['age']

age_not_survived.plot(kind='hist', bins=20, alpha=0.5, color='blue', label='No Supervivientes')


