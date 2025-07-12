import random
elementos = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890!#$%&/()=?¡¿abcdefghijklmnñopqrstuvwxyz"
tamaño = int(input("Escribe la cantidad de caracteres que va a tener la contraseña "))

contraseña =""

for i in range(tamaño):
    contraseña += random.choice(elementos)

print(contraseña)
