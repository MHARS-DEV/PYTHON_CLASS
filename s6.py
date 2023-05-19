class Vehiculo :
    color = "Rojo"
    Ruedas = 4
    Puertas = 4


class Coche(Vehiculo):
    
    velocidad = 100
    Cilindrada = 1000

auto = Coche 

print("El auto es de color :",auto.color)
print("Tiene",auto.Ruedas,"Ruedas nuevecitas")
print("Su Cilindrada es de",auto.Cilindrada)
