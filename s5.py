def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

consulta : int = int(input("Ingrese el año a consultar : "))
#print(es_bisiesto(consulta))
if(es_bisiesto(consulta)==True) : 
  print("El año ingresado es bisiesto")
elif(es_bisiesto(consulta)== False) :
    print("El año ingresado no es bisiesto")
