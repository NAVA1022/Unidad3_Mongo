'''
Unidad 3: Programación Orientada a objetos
Tema: 1.1 Clases y objetos
Fecha: 28 de septiembre del 2022
Autor: Carlos Israel Bautista Mejía

Clases y objetos en Python : https://www.youtube.com/watch?v=aj4PEXq0zuc
'''
import datetime
import random

'''
Sumar y restar dias a la fecha: https://j2logo.com/operaciones-con-fechas-en-python/
Generar numeros aleatorios: https://j2logo.com/python/generar-numeros-aleatorios-en-python/
Código ASCII:  https://elcodigoascii.com.ar/
Convertir un INT a ASCII: https://www.delftstack.com/es/howto/python/python-int-to-ascii/
Descargue la libreria bcrypt con el comando: "pip install bcrypt"

Realizar una clase llamada Password que siga las siguientes condiciones:
▪ Que tenga los atributos longitud, contraseña y fecha_expiracion. Por defecto, la longitud sera de 8, la contraseña
  será los números del 1 al 8 y la fecha_expiración será de UN día.
  
▪ Un constructor con la contraseña y fecha_expiracion que nosotros le pasemos, se calculará la longitud de la contrasena

Generará una contraseña aleatoria con esa longitud.

▪ Los métodos que implementa serán:
▪ esFuerte(): devuelve un booleano si es fuerte o no, para que sea fuerte debe tener mas de 2 mayúsculas, al menos una
minúscula y al menos  1 caracter.

▪ generarPassword(): genera la contraseña del objeto con la longitud que tenga.

▪ cifraPassword(): cifra la contraseña del objeto.

▪ verificarClave: regresará verdadero si la contrasena es correcta.

▪ Método get para contraseña y longitud.

▪ Método set para longitud.

Ahora, crea una clase clase ejecutable(main):
▪ Crea un array de Passwords con el tamaño que tu le indiques por teclado.
▪ Crea un bucle que cree un objeto para cada posición del array.
▪ Indica también por teclado la longitud de los Passwords (antes de bucle).
▪ Crea otro array de booleanos donde se almacene si el password del array de Password es o no fuerte (usa el bucle anterior).
▪ Al final, muestra la contraseña y si es o no fuerte (usa el bucle anterior). Usa este simple formato:
contraseña1 valor_booleano1
contraseña2 valor_bololeano2
'''
import datetime

class Password:
    # Constructo longitud, contraseña y fecha exacta
    def __init__(self, contrasena = '123456789', longitud = 8, fecha_exp = datetime.date.today()):
        self.longitud = longitud
        self.contrasena = contrasena
        self.contrasena_cifrada = self.Cifrar_password()
        self.fecha_expiracion = fecha_exp + datetime.timedelta(days = 1)

    # Método es_fuerte. 2 mayúsculas, al menos 1 minúscula y 1 caracter.
    def es_fuerte(self):
        cont_mayus = 0
        cont_min = 0
        cont_caract = 0
        cont_num = 0

        for car in self.contrasena:
            if ord(car) >= 65 and ord(car) <= 90: # Letra mayúscula
                cont_mayus += 1
            elif ord(car) >= 98 and ord(car) <= 122:
                cont_min +=1
            elif ord(car) >= 48 and ord(car) <= 57:
                cont_num += 1
            else:
                cont_caract += 1

        if cont_mayus >= 2 and cont_min >= 1 and cont_caract >= 1:
            return True
        return False

    def __str__(self):
        return f"Contraseña: {self.contrasena} Contraseña Cifrada: {self.contrasena_cifrada}"

    def generar_mayusculas(self):
        # Generar letras mayusculas de forma aleatoria
        return chr(random.randint(65,90))

    def generar_minusculas(self):
        # Generar letras minúsculas de forma aleatoria
        return chr(random.randint(98,122))

    def generar_numeros(self):
        # Generar numeros de forma aleatoria
        return chr(random.randint(48, 57))

    def generar_caracteres(self):
        # Generar caracteres especiales de forma aleatoria
        lista = ['?', '*', '!', '#', '$', '%', '&', '¿', '¡', '@']
        return lista[random.randint(0, 9)]

    def gen_pass(self):
        cve = ""
        for i in range(self.longitud):
            # Generar aleatoriamente números del 1 al 4
            num = random.randint(1, 4)
            if num == 1: # Genera letras mayúsculas
                cve += self.generar_mayusculas()
            elif num == 2: # Genera letras minúsculas
                cve += self.generar_minusculas()
            elif num == 3: # Genera números
                cve += self.generar_numeros()
            elif num == 4: # Genera caracteres especiales
                cve += self.generar_caracteres()
        self.contrasena = cve
        self.contrasena_cifrada = self.Cifrar_password()
        return cve

    def Cifrar_password(self):
        import bcrypt
        sal = bcrypt.gensalt()  # Default tiene de 12
        return bcrypt.hashpw(self.contrasena.encode(), sal)

    def decifrar_password(self, password, password_decrypt):
        import bcrypt
        if bcrypt.checkpw(password.encode("utf-8"), password_decrypt):
            return True
        return False

def app():
    pws = []
    arr_fuertes = []
    num_elem = int(input("Dame cuantos elementos quieres: "))
    longitud = int(input("Dame la longitud: "))

    for i in range(num_elem):
        objPassword = Password(longitud = longitud)
        objPassword.gen_pass()
        pws.append(objPassword)
        arr_fuertes.append(objPassword.es_fuerte())

    for i in range(num_elem):
        print(pws[i].contrasena, arr_fuertes[i])

# app()

# objPassword = Password(contrasena= "HOLA.123")
# password = objPassword.gen_pass()
# password_encrypted = objPassword.Cifrar_password(password)
# decrypt = objPassword.decifrar_password(password, password_encrypted)
# print(f"Clave: {password}\nCifrada: {password_encrypted} \nCoinciden: {decrypt}")
# print(f"\n{objPassword.contrasena}")

# objPassword = Password(contrasena="HOla@123")
# print(objPassword)
# objPassword.gen_pass()
# print()
# print(objPassword)
# print(objPassword.es_fuerte())


