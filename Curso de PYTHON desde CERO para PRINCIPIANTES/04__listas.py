### Lists ###

# Definición
my_list = list()
my_other_lists = []

print(len(my_list))

my_list = [62, 54, 63, 30, 17, 30, 72]

print(my_list)
print(len(my_list))

my_other_lists = [29, 1.81, "Jesus", "Chiroque"]
print(my_other_lists)
print(type(my_other_lists))

# Acceso a elementos y búsqueda
print(my_other_lists[0])
print(my_other_lists[1])
print(my_other_lists[-1])
print(my_other_lists[-4])
print(my_list.count(30))
# print((my_other_lists[4])) IndexError
# print((my_other_lists[-5])) IndexError
print(my_other_lists.index("Jesus"))

age, height, name, surname = my_other_lists
print(name)

name, height, age, surname = my_other_lists[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación
print(my_list + my_other_lists)
# print(my_list - my_other_lists)

# Creación, inserción, actualización y eliminación
my_other_lists.append("ChiroqueSAC")
print(my_other_lists)

my_other_lists.insert(1, "Rojo")
print(my_other_lists)

my_other_lists[1] = "Azul"

my_other_lists.remove("Azul")
print(my_other_lists)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas
print(my_new_list[1:3])

# Cambio de tipo
my_list = "Hola Python"
print(my_list)
print(type(my_list))