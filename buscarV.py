'''i=int(input("ingrese inicio de columnas = "))
x=int(input("ingrese columnas = "))
while x<i and i<0:
    i=int(input(f"ingrese un numero mayor a 0\n o mayor a {x} ")) '''
sw=1
while sw == 1:
    x=int(input("ingrese columnas = "))
    y=x+1

    for i in range(y):
        if i == 0 or i == 1:
            print("")
        else:
            a = f'"=BUSCARV(AN{i};AO13:AO33047;1;0)",'
            print(a)
    sw=int(input("¿desea seguir buscando?\n.-1 si\n.-2 no = "))
    if sw==1:
        sw=1
    else:
        sw=0
        print("bye")