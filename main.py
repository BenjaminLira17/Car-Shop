from carro import *
from persona import *
from helpers import*
from re import match
import sys
from datetime import date
import random
today = date.today()
cliente_def = 0
valor_productos = 0
tax = 0
total = 0
registrado =0
autos_en_carro= []
mis_autos_obj = []
rut = input("Ingrese su rut: ")
while bool(match("^[A-Za-z0-9]*$", rut)) == False:
  rut = input("Ingrese su rut (sin puntos ni guion ni espacios): ")
archivo = open("clientes.txt", "r").read().splitlines()
for i in archivo:
  a = i.split(",")
  if rut == a[0]:
    registrado +=1
    print("\nYa estas en nuestra base de datos!")
    advance()
    nombre = a[1]
    genero = a[2]
    email = a[3]
    direccion = a[4]
    cliente1 = Cliente(nombre, genero, rut, email, direccion)

if registrado == 0:
  print("\nHola, eres nuevo, te invitamos a registrarte!\n")
  nombre = input("Hola, bienvenido a la Tienda de Autos, Ingrese su nombre: ")
  while bool(match("^[A-Za-z ]*$", nombre)) == False:
    print("Nombre debe contener solo caracteres alphabeticos.")
    nombre = input("Hola, Bienvenido a la tienda de Autos, Ingrese su nombre: ")
  
  direccion = input("Ingrese su direccion para enviar sus productos: ")

  genero = input("Ingrese su genero: ").title()
  while genero not in ("Masculino", "Femenino"):
    genero = input("Ingrese su genero (Masculino o Femenino): ").title()
  
  email = input("Ingrese su e-mail: ")
  with open("clientes.txt", "a") as file:
    file.write(f"{rut},{nombre},{genero},{email},{direccion}\n")
  cliente1 = Cliente(nombre, genero, rut, email, direccion)
  advance()

def main():
  valor_productos = 0
  tax = 0
  total = 0
  descuento_count = 0
  descuento =0
  while True:
    cl()
    print("Tienda de Autos")
    print("""\n1) Ver Autos
2) Carro
3) Informacion de Vendedores
4) FAQ
5) Exit""")
    nav = input("\nNavegar a (1/2/3/4/5): ")
    while nav not in ("1", "2", "3", "4", "Esta es la mejor tienda!", "5"):
      nav = input("Navegar a (1/2/3/4/5): ")
    if nav == "1":
      cl()
      (a, b, c, index) = productos(autos)
      valor_productos += a
      tax +=b
      total+=c
      
      for i in range(len(index)):
        mis_autos_obj.append(autos[index[i]])
      carro = Carro(total, valor_productos, mis_autos_obj, tax, descuento, today, cliente1, nuevo_vendedor)
      

    elif nav == "2":
      if len(mis_autos_obj) == 0:
        print("\nThere is nothing in your cart")
        advance()
      else:
        vp, tx, t = carro_f(carro)
        valor_productos += vp
        tax +=tx
        total+=t
        carro = Carro(total, valor_productos, mis_autos_obj, tax, descuento, today, cliente1, nuevo_vendedor)
        
    elif nav == "3":
      
      print("\nInformacion de su vendedor:\n")
      nuevo_vendedor.getInfo()
      nuevo_vendedor.getCodigo()
      advance()
    elif nav == "4":
      print("""\nComo me comunico con la tienda para una consulta?
Solo tiene que escribir al mail, tienda_de_autos@gmail.com.
      
Puedo cambiar a mi vendedor?
No puede cambiar a su vendedor para que no sea injusto para algun vendedor discriminado.
      
Hay alguna manera de recibir un descuento?
Si, solo debe escribir en el menu textualmente 'Esta es la mejor tienda de autos!'""")
      advance()
    elif nav == "5":
      print("Una pena verlo ir sin ninguna compra, ojala vuelva algun dia!")
      sys.exit()
    else:
      if descuento_count == 0:
        print("\nHas encontrado la ruleta de DESCUENTO!")
        advance()
        descuento = round(random.uniform(0.01, 0.1), 2)

        print(f"\nTu descuento es de {round(descuento*100)}%")
        
        print("Será aplicado en el final de su compra.")
        advance()
        descuento_count +=1
        if len(mis_autos_obj) > 0:
          carro = Carro(total, valor_productos, mis_autos_obj, tax, descuento, today, cliente1, nuevo_vendedor)
      
    


def productos(lista):
  print("\nAutos\n")
  x=0
  for i in autos:
    x+=1
    print(x)
    i.getInfo()
  print("1) Menu / 2) Agregar al carrito")
  nav = navegation("Navegar a (1/2): ", 2)
  if nav == "1":
    cl()
    return 0,0,0,[]
  else:
    a=0
    b=0
    c=0
    index = []
    index_full = []
    while True:

      producto = input("Que auto desea agregar a su carro?: ")
      while not producto.isnumeric():
        producto = input("Que auto desea agregar a su carro?(1-7): ")
      producto = int(producto)
      while producto not in range(1,8):
        print("Este auto no se encuentra en nuestra tienda.")
        producto = input("Que auto desea agregar a su carro?(1-7): ")   
      producto -=1
      if producto in index:
        autos[producto].cantidad +=1
        index.remove(producto)
      if autos[producto] in mis_autos_obj:
        autos[producto].cantidad +=1
        del mis_autos_obj[producto]
      index_full.append(producto)
      index.append(producto)
      #total+=precio de auto
      choice = navegation("Desea agregar otro producto a su carro?(1 = si / 2 = no): ", 2)
      if choice == "2":
        break   
    for i in index_full:
      for x in range(len(autos)): 
        if i == x:
          a += autos[i].getVP()
          b += autos[i].getTax()
          c += autos[i].getTotal()
    index1 = index.copy()
    index.clear()
    index_full.clear()
    cl()
    return a,b,c,index1

#Finalizar Compra
def carro_f(carro):
  cl()
  carro.total = round(carro.total - carro.total*carro.descuento)
  print("\nTus Productos: \n")
  
  for i in range(len(mis_autos_obj)):
    carro.getProductos(i, "\n")
    print("Cantidad: ", carro.getCantidad(i), end= "\n\n")
  carro.getInfo()
  
  print("1) Menu / 2) Editar carro de compras / 3) Finalizar compra")
  nav = navegation("Navegar a (1/2/3): ", 3)
  if nav == "2":
    cl()
    ilist=[]
    print()
    for i in range(0,len(mis_autos_obj)):
      ilist.append(str(i+1))
      print(f"{i+1}) ")
      carro.getProductos(i, "\n")
      print("Cantidad: ", carro.getCantidad(i), end= "\n\n")
    delete = input("Que auto quisieras quitar de tu carro de compras? Presione el numero encima del auto a quitar: ")
    while delete not in ilist:
      print("Este numero no ha llegado a ningun auto")
      delete = input("Que auto quisieras quitar de tu carro de compras? Presione el numero al lado del auto a quitar: ")
    delete = int(delete)-1
    precio = mis_autos_obj[delete].precio
    vp = -mis_autos_obj[delete].getVP()
    tx = -mis_autos_obj[delete].getTax()
    t = -mis_autos_obj[delete].getTotal()
    if mis_autos_obj[delete].cantidad != 1:
      mis_autos_obj[delete].cantidad -=1
    else:
      del mis_autos_obj[delete]
    return vp, tx, t
    
    
  elif nav == "3":
    
    tarjeta = input("\nIngrese su numero de tarjeta de crédito: ")
    cliente1.setTarjeta(tarjeta)
    print("\nSu informacion: \n")
    cliente1.getInfo()
    cliente1.getTarjeta()
    print("Información de su vendedor: \n")
    nuevo_vendedor.getInfo()
    nuevo_vendedor.getCodigo()
    confirm = navegation("Desea confirmar su compra? (si = 1/ 2 = no): ", 2)
    if confirm == "1":
      with open("ventas.txt", "a") as file:
        file.write(f"{cliente1.getRut()}, {', '.join(carro.getNombrePructos())}, {carro.total}, {carro.fecha}\n")
      print(f"Muchas gracias {nombre} por la compra! Que usted tenga un buen dia!")
      sys.exit()
  return 0,0,0

if __name__ == "__main__":
  main()
