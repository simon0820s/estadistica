from tabClass import Tabla
def main():
    lista=[]
    n=int(input("cuantos datos desea ingresar? "))

    for i in range(0,n):
        ent=input("ingrese el dato #"+str(i+1)+" ")
        lista.append(ent)

    tabla=Tabla(lista)
    print(tabla.printTab())


if __name__=='__main__':
    main()

