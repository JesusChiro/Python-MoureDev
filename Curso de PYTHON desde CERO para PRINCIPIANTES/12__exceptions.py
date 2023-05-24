### Exception Handling ###

n1, n2 = 5, 1
n2 = "1"

# Excepción base: try except

try:
    print(n1 + n2)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:
    print(n1 + n2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecucion continúa")


# Excepciones por tipo

try:
    print(n1 + n2)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepcion

try:
    print(n1 + n2)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as error:
    print(error)