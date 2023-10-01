import random

contra = []
char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

for i in range(3):
    long = int(input("dime la longitud de la contraseña: "))
    password = ""
    for i in range(long):
        element = random.choice(char)
        password += element
    print("tu contraseña generada fue: ", password)
    almacenar = input("quieres almacenar esta contraseña(SI / NO): ")
    if almacenar == "SI":
        contra.append(password)
        print("estas son tus contraseñas: ", contra)
    elif almacenar == "NO":
        print("muy bien, no la voy a guardar")
    else:
        print("no entendi")