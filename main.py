class Persona:
  def __init__ (self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido


class Cliente(Persona):
  

  def __init__(self, numero_cuenta, cantidad):
    self.numero_cuenta = numero_cuenta
    self.cantidad = cantidad
    

  def retirar (self):
     cantidad_retirar = input("cuánto dinero quieres retirar: ")
     self.cantidad = self.cantidad - cantidad_retirar
     print(f"Tienes {self.cantidad} euros.")
 
  def insertar (self):
     cantidad_insertar = input("cuánto dinero quieres retirar: ")
     self.cantidad = self.cantidad + cantidad_insertar
     print(f"Tienes {self.cantidad} euros.")

  def consultar(self): 
    print(f"{self.nombre} {self.apellido} tienes {self.cantidad} euros.")
