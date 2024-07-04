import random
x=3


while x > 0:

    try:

        pregunta = int(input("¿cual crees que es el numero?:"))
    except:
        print("¡Solo se pueden ingresar números!")
        continue

    numero=random.randint(0,1000000000)
    print(numero)


    if pregunta == numero:
        print(f"\n!FELIZIDADES¡ acertaste el numero {numero}")
        break

    else:
        x -= 1
        print(f"\nperdiste tienes {x} intentos\n")



if x == 0:
    print("perdiste")