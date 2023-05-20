import pickle
f=open('fichero.txt','w')
f.write("Mi nombre es Alexander\n")
f.close()

f=open('fichero.txt','a')
f.write("Mi apellido es Matos Huaroc\n")
f.close()

f=open('fichero.txt','r+')
print(f.read())
f.close()

