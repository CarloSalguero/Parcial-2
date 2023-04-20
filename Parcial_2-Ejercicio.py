print("Parcial_2 - Ejercicio practico.")

Num = input("\nIngrese el numero entero a procesar: ")

Com = True

while Num.isdigit() != True:
    print("Error el numero ingresado es incorrecto\n")
    Num = input("Ingrese el numero entero a procesar: ")

Num = int(Num)

valor = 0
for i in range(Num):
    i = i + 1
    print(1,"/", i)
    valor += 1/i

print("Su resultado es:", valor)
