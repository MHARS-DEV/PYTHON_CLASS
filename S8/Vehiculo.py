class vehiculo :
   
    def __init__ (self,color,marca) : 
        self.color = color
        self.marca = marca

carrito = vehiculo("NEGRO","LAMBORGUINI")

#print(f'El carro es color {carrito.color} y la marca es {carrito.marca}' )

f=open('guardaCaracteristicas.txt',"w")
texto=f'Color : {carrito.color} y la marca es :{carrito.marca}'
f.write(texto)
f.close()

f=open('guardaCaracteristicas.txt',"r+")
print(f.read())
f.close()



