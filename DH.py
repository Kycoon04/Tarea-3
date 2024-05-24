def es_primo(n): #Esto es un metodo normal para ver si es primo o no
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def obtener_primo():
    while True:
        primo = int(input("Ingrese un número primo: "))
        if es_primo(primo):
            return primo
        print("El número no es primo, por favor ingrese otro.")

def obtener_base(primo):
    while True:
        base = int(input(f"Ingrese una base para {primo}: "))
        if 1 < base < primo - 1:
            return base
        print(f"La base no es válida para {primo}, intente de nuevo.")

def obtener_clave_privada(nombre_usuario, primo):
    while True:
        clave = int(input(f"Ingrese la clave privada del {nombre_usuario}: "))
        if clave < primo:
            return clave
        print(f"La clave privada debe ser menor que {primo}, intente de nuevo.")

def calcular_clave_publica(clave_privada, base, primo):
    return pow(base, clave_privada, primo) #(base^(clave_privada) % primo)

def calcular_clave_secreta(clave_publica_propia, clave_privada_ajena, primo):
    return pow(clave_publica_propia, clave_privada_ajena, primo) #(clave_publica_propia^(clave_privada_ajena) % primo)

def intercambio_claves(k1, k2):
    return k1 == k2

if __name__ == "__main__":

    nombre_usuario1 = input("Ingrese el nombre del Usuario 1: ")
    nombre_usuario2 = input("Ingrese el nombre del Usuario 2: ")

    primo = obtener_primo()
    base = obtener_base(primo)

    clave_privada_usuario1 = obtener_clave_privada(nombre_usuario1, primo)
    clave_privada_usuario2 = obtener_clave_privada(nombre_usuario2, primo)

    clave_publica_usuario1 = calcular_clave_publica(clave_privada_usuario1, base, primo)
    clave_publica_usuario2 = calcular_clave_publica(clave_privada_usuario2, base, primo)

    print(f"\nLa clave pública para {nombre_usuario1} es {clave_publica_usuario1}")
    print(f"La clave pública para {nombre_usuario2} es {clave_publica_usuario2}")

    clave_secreta_usuario1 = calcular_clave_secreta(clave_publica_usuario2, clave_privada_usuario1, primo)
    clave_secreta_usuario2 = calcular_clave_secreta(clave_publica_usuario1, clave_privada_usuario2, primo)

    print(f"\nLa clave secreta para {nombre_usuario1} es {clave_secreta_usuario1}")
    print(f"La clave secreta para {nombre_usuario2} es {clave_secreta_usuario2}\n")

    if intercambio_claves(clave_secreta_usuario1, clave_secreta_usuario2):
        print("Las claves se han intercambiado con éxito.")
    else:
        print("Las claves no se han intercambiado con éxito.")