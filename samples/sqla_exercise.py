from sqlalchemy.orm import declarative_base
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Crear una conexión a una base de datos SQLite
engine = create_engine('sqlite:///mi_base_de_datos.db')
print("Conexión establecida con éxito")


# Crear una base declarativa
Base = declarative_base()

# Definición del modelo
# survived,pclass,sex,age,sibsp,parch,fare,embarked,class,who,adult_male,deck,embark_town,alive,alone
# 0,3,male,22.0,1,0,7.25,S,Third,man,True,,Southampton,no,False
class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer, primary_key=True)
    survived = Column(Integer)
    pclass = Column(Integer)
    sex = Column(String)
    age = Column(Integer)
    sibsp = Column(Integer)
    parch = Column(Integer)
    fare = Column(Integer)
    embarked = Column(String)
    class_ = Column(String)
    who = Column(String)
    adult_male = Column(Boolean)
    deck = Column(String)
    embark_town = Column(String)
    alive = Column(String)
    alone = Column(Boolean)


Base.metadata.create_all(engine)
print("Tablas creadas con éxito")

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# read csv with pandas
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

# check if the table is empty
passengers = session.query(Passenger).all()
if passengers:
    print("La tabla 'passengers' no está vacía.")
else:
# Insertar datos en la tabla
    for index, row in df.iterrows():
        # # survived,pclass,sex,age,sibsp,parch,fare,embarked,class,who,adult_male,deck,embark_town,alive,alone
        passenger = Passenger( 
            survived=row['survived'], 
            pclass = row['pclass'], 
            sex = row['sex'], 
            age = row['age'],
            sibsp = row['sibsp'],
            parch = row['parch'],
            fare = row['fare'],
            embarked = row['embarked'],
            class_ = row['class'],
            who = row['who'],
            adult_male = row['adult_male'],
            deck = row['deck'],
            embark_town = row['embark_town'],
            alive = row['alive'],
            alone = row['alone']
        )
        session.add(passenger)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error al crear el registro: {e}")
    print("Registros creados con éxito")

# funcrion that gets all passengers from the table as dataframe with all columns
def get_passengers_df():
    # lee los registros de la tabla
    passengers = session.query(Passenger).all()
    # convierte a dataframe
    # survived,pclass,sex,age,sibsp,parch,fare,embarked,class,who,adult_male,deck,embark_town,alive,alone
    df = pd.DataFrame([{
        'ID': passenger.id,
        'survived': passenger.survived,
        'pclass': passenger.pclass,
        'sex': passenger.sex,
        'age': passenger.age,
        'sibsp': passenger.sibsp,
        'parch': passenger.parch,
        'fare': passenger.fare,
        'embarked': passenger.embarked,
        'class': passenger.class_,
        'who': passenger.who,
        'adult_male': passenger.adult_male,
        'deck': passenger.deck,
        'embark_town': passenger.embark_town,
        'alive': passenger.alive,
        'alone': passenger.alone} for passenger in passengers])
    return df

# lee los registros de la tabla
df = get_passengers_df()
print(df.shape)