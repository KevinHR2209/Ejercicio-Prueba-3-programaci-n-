#EL CODIGO ESTÁ MÁS QUE COMENTADO, IGUAL CUALQUIER DUDA O SUGERENCIA ME DICE, PERO TODAS LAS OPCIONES FUNCIONAN
#SOBRE LAS FUNCIONES HICE SOLO DOS, PORQUE DESPUES SOLO LLAMO A LOS VALORES OBTENIDOS EN LA EJECUCIÓN DE CADA UNA DE ELLAS
#DEJEN MI CODIGO EN SECRETO UWU

#Ejercicio Prueba 3 Menu + Funciones#
def imprimir_asientos(escenario, numero_filas): #Dos parametros escenario que es la lista de elementos y numero de filas que indica la forma en que se van a distribuir
    asientos = [] #Lista para almacenar los asientos con el número o con una X dependiendo el caso
    for elemento in escenario: #Bucle para recorrer cada elemento de la lista escenario
        if elemento == 0: #Si el elemento de la lista es 0 lo reemplaza con una X porque está ocupada
            asientos.append("X")
        else:
            asientos.append(str(elemento)) #Si el elemento no es 0, lo reemplaza por una cadena de texto que corresponde al numero del asiento
    print("\t\t\t    ESCENARIO")
    asientos_por_fila = len(asientos) // numero_filas #Calcula cuando asientos habra por fila
    if asientos_por_fila == 0:
        print("El número de filas no puede ser cero o mayor al número de asientos.")
        numero_filas=int(input("Intente nuevament ingresando un número válido de filas: "))
        asientos_por_fila = len(asientos) // numero_filas
    for filas in range(0, len(asientos), asientos_por_fila): #Bucle for para que se haga sobre la lista de asientos en base al tamaño de asiento por fila
        for asiento in asientos[filas:filas + asientos_por_fila]: #Bucle for para recorrer en base al tamño de asientos por fila, esto hace que se muestren la cantidad de filas y asientos
            print(asiento, end="\t\t") #Imprime lo anterior con una tabulación
        print() #Hace el salto de linea cada vez que se termina de imprimir una linea


def valor_asientos(escenario,numero_filas):
    precio_asientos = {} #Almacenará cada asiento con su respectivo precio
    for asiento in escenario: #Se itera sobre cada asiento 
        if 1 <= asiento < ultimo_asiento_vip: #Dependiendo el rango se asigna precio para entrada vip
            precio_vip = valor_entradas_vip
            precio_asientos[asiento] = precio_vip
        elif ultimo_asiento_vip+1 <= asiento < ultimo_asiento_normal: #Dependiendo el rango se asigna precio para entrada normal
            precio_normal = valor_entradas_normal
            precio_asientos[asiento] = precio_normal
        elif ultimo_asiento_normal+1 <= asiento <= cantidad_asientos: #Dependiendo el rango se asigna precio para entrada barata
            precio_barato = valor_entradas_baratas
            precio_asientos[asiento] = precio_barato
    cantidad_a_comprar = int(input("Ingrese la cantidad de entradas a comprar: ")) #Se solicita la cantidad a comprar hasta que sea mayor a 0 o menor igual a 2
    while cantidad_a_comprar < 1 or cantidad_a_comprar > 2: 
        print("La cantidad máxima a comprar son 2")
        print("Intente nuevamente")
        cantidad_a_comprar=int(input("Ingrese la cantidad de entradas a comprar:"))
    for numero_comprar in range(cantidad_a_comprar): #Bucle para poder comprar entradas
        asiento_comprar = 0
        while asiento_comprar == 0 or escenario[asiento_comprar - 1] == 0: 
            imprimir_asientos(escenario, numero_filas) #Se muestra el escenario con los asientos disponibles y ocupados
            asiento_comprar = int(input("Ingresa el asiento que quieres comprar: "))
            if escenario[asiento_comprar - 1] == 0: #Si el asiento esta ocupadao se informa al usuario para que intente de nuevo
                print("El asiento no está disponible, intente con otro asiento.")
                asiento_comprar = 0
        escenario[asiento_comprar - 1] = 0 #Si el asiento estaba disponible ahora se asignará como NO disponible
        precio = precio_asientos[asiento_comprar] #Se obtiene el precio del asiento en base al número del asiento (clave, valor)
        run = int(input("Ingrese el RUN de la persona que ocupará el asiento (sin guión ni puntos): ")) #Pide el run del comprador
        print(f"Se ha comprado el asiento {asiento} por ${precio} para el RUN {run}.\n")
        lista_run.append(run) #Se guarda el run en la lista
        lista_ganancias.append(precio) #Se guarda el precio en la lista
    return precio_asientos


lista_run = [] #Lista que almacena los ruts para despues poder imprimirla
lista_ganancias=[] #Lista que almacena las ganancias para despues poder imprimirla


#Validación de datos para el concierto
print("Bienvenido al Sistema de ventas para el concierto de XXXXXXXXXX")
print
print("Antes de comenenzara con el proceso de venta, necesitamos validar unos datos")
cantidad_asientos = int(input("Ingrese la cantidad de asientos que tiene el concierto: ")) #Pide la cantidad de asientos para el concierto
escenario = list(range(1, cantidad_asientos + 1)) #List para poder agregar los elementos a la lista del diccionario para la función 1
numero_filas = int(input("Ingrese el número de filas que tendrá el concierto: ")) #Pide la cantidad de filas que tendrá


while numero_filas <= 0 or numero_filas > cantidad_asientos:
    numero_filas = int(input("Ingrese el número de filas que tendrá el concierto: "))
    if numero_filas <= 0 or numero_filas > cantidad_asientos:
        print("El número de filas debe ser un número positivo y menor o igual a la cantidad de asientos.")
ultimo_asiento_vip=int(input("Ingrese el último asiento que pertenecerá a la categoría de VIP: ")) #Inica la posición del ultimo asiento vip
ultimo_asiento_normal=int(input("Ingrese el último asiento que pertenecerá a la categoría de NORMAL: ")) #Indica la posición del último asiento normal
valor_entradas_vip=int(input("Ingrese el precio en $ de las entradas VIP: ")) #Indica valor entrada vip
valor_entradas_normal=int(input("Ingrese el precio en $ de las entradas NORMALES: ")) #Indica valor entrada normal
valor_entradas_baratas=int(input("Ingrese el precio en $ de las entradas BARATAS: ")) #Indica valor entrada barata


#Todo esto es el Menú xd
while True: #Con esto hago que se repita de forma infinita hasta que se metan a la opción 6
    print()
    print("---------------MENÚ---------------")
    print("1) Comprar entradas")
    print("2) Ubicaciones disponibles")
    print("3) Lista de Usuarios que compraron entradas")
    print("4) Ganancia de ventas")
    print("5) Rut mayor y menor")
    print("6) Salir")
    print()
    opcion_menu=int(input("Ingrese la opción de su preferencia: ")) #Pide la opción de menú que quiere el usuario
    if opcion_menu <1 or opcion_menu >6: #En caso de ingresar una opción inválida pedirá volver a ingregar valor 
        print("Ingresó una opción inválida, intente nuevamente")
    else:
        match opcion_menu: #Ingresa a la opción en base a la opción que ingresó el usuario
            case 1:
                print("Decidió comprar entradas")
                valor_asientos(escenario,numero_filas) #Llama a la función en base a los parámetros pedidos antes
            case 2:
                print("Decidió consultar las ubicaciones disponibles")
                print("Las ubicaciones disponibles aparecen con el número respectivo")
                print("Las ubicaciones ocupadas aparecerán con una X")
                imprimir_asientos(escenario,numero_filas) #Llama a la función en base a los parámetros pedidos antes
            case 3:
                print("Esta es la lista de los usuarios que compraron entradas")
                print(lista_run) #Imprime la lista de ruts que compraron, cada vez que se compren entradas se actualiza uwu
            case 4:
                print("Esta es la ganancia obtenida por la venta de las entradas")
                print(f"La ganancia por la venta de entradas en total es de $ {sum(lista_ganancias)}") #Imprime la ganancia total de las entrada, cada vez que se compran entradas se actualiza
            case 5:
                print("Estas son las estadísticas de los rut que compraron entradas")
                print(f"El rut más alto que compró entrada es",max(lista_run)) #Muestra el run más alto
                print(f"El rut más bajo que compró entrada es",min(lista_run)) #Muestra el run más bajo
            case 6:
                print("MUCHAS GRACIAS POR UTILIZAR NUESTRO SISTEMA")
                print("\t\t ADIÓS")
                break
