### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:  # Es opcional
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecucion continúa")

# For

print("*" * 10 + "Ciclo For con Listas" + "*" * 10)
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

print("*" * 10 + "Ciclo For con Tuplas" + "*" * 10)
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

print("*" * 10 + "Ciclo For con Set" + "*" * 10)
my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)

print("*" * 6 + "Ciclo For con Diccionarios + break" + "*" * 6)
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario ha finalizado")
print("La ejecucion continúa")

print("*" * 6 + "Ciclo For con Diccionarios + continue" + "*" * 6)
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
