class Carro: 
  def __init__(self, total, valor_productos, productos, tax, descuento, fecha, cliente, vendedor):
    self.total = total
    self.valor_productos = valor_productos
    self.productos = productos
    self.tax = tax
    self.descuento = descuento
    self.fecha = fecha
    self.cliente = cliente
    self.vendedor = vendedor
  def getProductos(self, i, end ="\n\n"):
    self.productos[i].getInfo(end)
  def getNombrePructos(self):
    num = len(self.productos)
    list = []
    for i in range(num):
      list.append(f"{self.productos[i].cantidad} {self.productos[i].getNombre()}")
    return list

  def getCantidad(self, i):
    return self.productos[i].cantidad
  def getDescuento(self):
    return (f"Descuento: {self.descuento*100}%")
  def getInfo(self):
    print(f"""Direccion de envio: {self.cliente.direccion}  
Valor Productos: {self.valor_productos}
Impuestos: {self.tax}

Descuento: {round(self.descuento*100)}%
Total: {self.total}\n""")

class Auto:
  def __init__(self, marca, modelo, color, motor, precio, cantidad):
    self.marca = marca
    self.modelo = modelo
    self.color = color
    self.motor = motor
    self.precio = precio
    self.cantidad = cantidad
      
  def getInfo(self, ends="\n\n"):
    print(f"""Marca: {self.marca}
Modelo: {self.modelo}  
Color: {self.color}
Motor: {self.motor}
Precio: {self.precio}""", end = ends)
    
  def getNombre(self):
    return(f"{self.marca} {self.modelo}")
  def getVP(self):
    return self.precio
  def getTax(self):
    return round(self.precio*0.075)
  def getTotal(self):
    return round(self.precio*0.075 + self.precio)


autos = []

archivo = open("productos.txt", "r").read().splitlines()

for i in archivo:
  a = i.split(",")
  autos.append(Auto(a[0], a[1], a[2], a[3], int(a[4]), 1))



