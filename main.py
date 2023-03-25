class Persona:
  def __init__ (self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido


class Cliente(Persona):
  

  def __init__(self, nombre, apellido, numero_cuenta, cantidad = 0):
    super().__init__(nombre, apellido)
    self.numero_cuenta = numero_cuenta
    self.cantidad = cantidad
    

  def retirar (self, cantidad_retirar):
    if self.cantidad >= cantidad_retirar:
       self.cantidad = self.cantidad - cantidad_retirar
       print(f"Tienes {self.cantidad} euros.")
    else:
      print("Fondos insuficientes")
 
  def depositar (self, cantidad_depositar):
     self.cantidad = self.cantidad + cantidad_depositar
     print(f"Tienes {self.cantidad} euros.")

  def __str__(self): 
    return f"{self.nombre} {self.apellido} tienes {self.cantidad} euros."



def crear_cliente():
  nombre_cl = input("Ingrese su nombre: ")
  apellido_cl = input("Ingrese su apellido: ")
  numero_de_cuenta = input("Ingrese su numero de cuenta: ")
  cliente = Cliente(nombre_cl, apellido_cl, numero_de_cuenta)
  return cliente

def Inicio():
  mi_cliente = crear_cliente()
  print(mi_cliente)
  opcion = 0  
  while opcion != "s":
    print("Elije : Depositar(d)  retirar(r)  comprobar saldo(c)  salir(s)")
    opcion = input("")

    if opcion == "d":
      cantidad_dep = int(input("cuanto dinero quieres depositar: "))
      mi_cliente.depositar(cantidad_dep)   
    elif opcion == "r":
      cantidad_re = int(input("cuanto dinero quieres retirar: "))
      mi_cliente.retirar(cantidad_re)   
    elif opcion == "c":
      print(mi_cliente)

  print("Gracias por operar en banco Python")

Inicio()