### Conditionals ###

my_condiction = False

if my_condiction:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condiction = 5 * 5

if my_condiction == 10:
    print("Se ejecuta la condición del segundo if")

if my_condiction > 10 and my_condiction < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condiction == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


print("La ejecución continua")


my_string = ""

if not my_string:
    print("mi cadena de texto es vacía")

if my_string == "Mi cadena de textooooooo":
    print("Estas cadenas de texto coinciden")