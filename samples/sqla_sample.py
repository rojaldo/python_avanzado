from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

# Crear una conexión a una base de datos SQLite
engine = create_engine('sqlite:///mi_base_de_datos.db')
print("Conexión establecida con éxito")


# Crear una base declarativa
Base = declarative_base()

# Definición del modelo
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    edad = Column(Integer)

Base.metadata.create_all(engine)
print("Tablas creadas con éxito")



# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear un nuevo usuario
nuevo_usuario = Usuario(nombre='Juan', edad=30)

# Añadir el usuario a la sesión
session.add(nuevo_usuario)

# Confirmar los cambios
try:
    session.commit()
except Exception as e:
    session.rollback()
    print(f"Error al crear el registro: {e}")
print("Registro creado con éxito")

# lee los registros de la tabla
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Edad: {usuario.edad}")

usuario_a_actualizar = session.query(Usuario).filter_by(id=1).first()

# Modificar la edad
if usuario_a_actualizar:
    usuario_a_actualizar.edad = 31
    session.commit()
    print("Registro actualizado con éxito")
else:
    print("Usuario no encontrado")

# check if the user exists
usuario_a_eliminar = session.query(Usuario).filter_by(id=1).first()

# Eliminar el usuario
if usuario_a_eliminar:
    session.delete(usuario_a_eliminar)
    session.commit()
    print("Registro eliminado con éxito")
else:
    print("Usuario no encontrado")

# check number of users
usuarios = session.query(Usuario).count()
print(f"Total de usuarios: {usuarios}")

# Cerrar la sesión
session.close()
print("Sesión cerrada con éxito")
# Cerrar la conexión
engine.dispose()
print("Conexión cerrada con éxito")

# Ordenar usuarios por nombre
usuarios_ordenados = session.query(Usuario).order_by(Usuario.nombre.asc()).all()
for usuario in usuarios_ordenados:
    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Edad: {usuario.edad}")