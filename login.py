from moduloLogin import register

print ("Bienvenido al sistema!!!")

while True:
    option = input("\nElige una opcion: 1.Registrarse 2.Login 3.Salir\n")
    
    if option in ('1', '2', '3'):


        if option == '1':
            print ('///////////Registro///////////\n')
            usuario = input("Crear un usuario: ")
            contrasena = input("Crear una contrasena: ")
            print (register(usuario, contrasena))
                

        elif option == '2':
            print ('Login\n')

            inicio = user_exist(usuariologin, contrasenalogin)
            if inicio == True:
                print (f"Bienvenido {nombrelogin} {apellidologin}")
            else:
                print ("\nUsuario o contrasena incorrecta")

        elif option == '3':
            print ('Saliendo...')
            break
        else:
            print ('NUMERO INCORRECTO\n')
