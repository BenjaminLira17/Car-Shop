import random

class Persona:
  def __init__(self, nombre, genero, rut, email):
    self.nombre = nombre
    self.genero = genero
    self.__rut = rut
    self.email = email
  def getRut(self):
    return self.__rut
  def getInfo(self):
    print(f"""Nombre: {self.nombre}
Genero: {self.genero}
E-mail: {self.email}""")

class Vendedor(Persona):
  def __init__(self, nombre, genero, rut, email, codigo):
    Persona.__init__(self, nombre, genero, rut, email)
    self.codigo = codigo
  def getCodigo(self):
    print(f"Codigo: {self.codigo}\n")
  
     
class Cliente(Persona):
  def __init__(self, nombre, genero, rut, email, direccion):
    Persona.__init__(self, nombre, genero, rut, email)
    self.direccion = direccion
    self.__tarjeta = None
  def getTarjeta(self):
    print(f"Tarjeta: {self.__tarjeta}\n")
  def setTarjeta(self, tarjeta):
    self.__tarjeta = tarjeta
    
    
archivo = open("vendedores.txt", "r").read().splitlines()

v = random.choice(archivo).split(",")
nuevo_vendedor = Vendedor(v[0], v[1], v[2], v[3], v[4])

    