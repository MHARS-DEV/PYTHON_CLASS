class Alumno (): 

    def inicilizar(self,nombre,nota) :
        self.nombre = nombre
        self.nota = nota
    
    def imprimeDatos(self) :
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    def estado(self) :
        if self.nota < 12 :
            print ("El Alumno ha reprobado el curso")
        else : 
            print("El Alumno aprobó el curos")

estudiante=Alumno()

estudiante.inicilizar("Alexander",20)
estudiante.imprimeDatos()
estudiante.estado()


