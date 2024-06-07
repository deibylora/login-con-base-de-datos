from modulologin import registro, login

print ("Bienvenido a Facebook\n")

while True:

    print("\n---Menu principal---\n")

    menu = input("Elija una opcion: 1.Registrarse 2.Iniciar sesion 3.Salir\n")
    
    if menu in ('1', '2', '3'):
        if menu == '1':
            usuario_registro = input("Registre su usuario: ")
            contraseña_registro =input("Registre su contrasena: ")
            registro(usuario_registro, contraseña_registro)
            print (registro)
            
        elif menu == '2': 
            usuario_entrada = input("Ingrese su usuario: ")
            contraseña_entrada =input("Ingrese su contrasena: ")
            login(usuario_entrada, contraseña_entrada)
            print(login)

        elif menu == '3':
            print("Saliendo...")
            break
        
        else:
            print("Elije una opcion valida")