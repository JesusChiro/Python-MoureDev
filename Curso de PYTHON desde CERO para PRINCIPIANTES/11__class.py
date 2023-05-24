### Class ###


class MyEmptyPerson:
    pass


print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.fullname = f"{name} {surname} ({alias})"  # Propiedad publica
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.fullname} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.fullname)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.fullname)
my_other_person.walk()
my_other_person.fullname = "Héctor de León (El loco de los perros)"
print(my_other_person.fullname)

my_other_person.fullname = 666
print(my_other_person.fullname)
