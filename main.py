from tabClass import Tabla
def main():
    lista=[]
    name=input("ingrese el nombre de su tabla: ")
    n=int(input("cuantos datos desea ingresar? "))

    for i in range(0,n):
        ent=input("ingrese el dato #"+str(i+1)+" ")
        lista.append(ent)

    tabla=Tabla(name,n,lista)
    print(tabla.printTab())


if __name__=='__main__':
    main()

