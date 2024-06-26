def imprimir_asientos(escenario, numero_filas): 
    asientos = [] 
    for elemento in escenario:
        if elemento == 0: 
            asientos.append("X")
        else:
            asientos.append(str(elemento))
    print("\t\t\t    ESCENARIO")
    asientos_por_fila = len(asientos) // numero_filas 
    for filas in range(0, len(asientos), asientos_por_fila):
        for asiento in asientos[filas:filas + asientos_por_fila]:
            print(asiento, end="\t\t") 
        print()

def valor_asientos(escenario, numero_filas, entradas_vendidas, entradas_por_usuario, ganancias_por_tipo):
    precio_asientos = {} 
    for asiento in escenario: 
        if 1 <= asiento < 20: 
            precio_vip = 10000000
            precio_asientos[asiento] = precio_vip
        elif 21 <= asiento < 30: 
            precio_normal = 1000000
            precio_asientos[asiento] = precio_normal
        elif 31 <= asiento <= cantidad_asientos: 
            precio_barato = 1000
            precio_asientos[asiento] = precio_barato
    cantidad_a_comprar = int(input("Ingrese la cantidad de entradas a comprar: "))
    while cantidad_a_comprar < 1 or cantidad_a_comprar > 2: 
        print("La cantidad máxima a comprar son 2")
        print("Intente nuevamente")
        cantidad_a_comprar=int(input("Ingrese la cantidad de entradas a comprar:"))
    for numero_comprar in range(cantidad_a_comprar):
        asiento_comprar = 0
        while asiento_comprar == 0 or escenario[asiento_comprar - 1] == 0: 
            imprimir_asientos(escenario, numero_filas) 
            asiento_comprar = int(input("Ingresa el asiento que quieres comprar: "))
            if escenario[asiento_comprar - 1] == 0: 
                print("El asiento no está disponible, intente con otro asiento.")
                asiento_comprar = 0
        escenario[asiento_comprar - 1] = 0 
        precio = precio_asientos[asiento_comprar] 
        run = int(input("Ingrese el RUN de la persona que ocupará el asiento (sin guión ni puntos): ")) 
        print(f"Se ha comprado el asiento {asiento_comprar} por ${precio} para el RUN {run}.\n")
        lista_run.append(run) 
        lista_ganancias.append(precio) 
        if 1 <= asiento_comprar < 20:
            entradas_vendidas['vip'] += 1
            ganancias_por_tipo['vip'] += precio
        elif 21 <= asiento_comprar < 30:
            entradas_vendidas['normal'] += 1
            ganancias_por_tipo['normal'] += precio
        else:
            entradas_vendidas['barata'] += 1
            ganancias_por_tipo['barata'] += precio
        if run in entradas_por_usuario:
            entradas_por_usuario[run] += 1
        else:
            entradas_por_usuario[run] = 1
    return {'precio_asientos': precio_asientos, 'entradas_vendidas': entradas_vendidas, 'entradas_por_usuario': entradas_por_usuario, 'ganancias_por_tipo': ganancias_por_tipo}

lista_run = [] 
lista_ganancias=[] 
print("Bienvenido al Sistema de ventas para el concierto de XXXXXXXXXX")
print
cantidad_asientos = 50 
escenario = list(range(1, cantidad_asientos + 1)) #
numero_filas = 10 
entradas_vendidas = {'vip': 0, 'normal': 0, 'barata': 0}
entradas_por_usuario = {}
ganancias_por_tipo = {'vip': 0, 'normal': 0, 'barata': 0}

while True: 
    print()
    print("---------------MENÚ---------------")
    print("1) Comprar entradas")
    print("2) Ubicaciones disponibles")
    print("3) Lista de Usuarios que compraron entradas")
    print("4) Ganancia de ventas")
    print("5) Rut mayor y menor")
    print("6) Salir")
    print("7) Cantidad de entradas vendidas por tipo")
    print("8) Cantidad de entradas compradas por cada usuario")
    print("9) Usuario que compró más y menos entradas")
    print("10) Ganancia por cada tipo de entrada")
    print("11) Cantidad de asientos vendidos y no vendidos")
    print()
    opcion_menu=int(input("Ingrese la opción de su preferencia: ")) 
    if opcion_menu <1 or opcion_menu >11: 
        print("Ingresó una opción inválida, intente nuevamente")
    else:
        match opcion_menu: 
            case 1:
                print("Decidió comprar entradas")
                resultados = valor_asientos(escenario, numero_filas, entradas_vendidas, entradas_por_usuario, ganancias_por_tipo) 
                entradas_vendidas = resultados['entradas_vendidas']
                entradas_por_usuario = resultados['entradas_por_usuario']
                ganancias_por_tipo = resultados['ganancias_por_tipo']
            case 2:
                print("Decidió consultar las ubicaciones disponibles")
                print("Las ubicaciones disponibles aparecen con el número respectivo")
                print("Las ubicaciones ocupadas aparecerán con una X")
                imprimir_asientos(escenario,numero_filas) 
            case 3:
                print("Esta es la lista de los usuarios que compraron entradas")
                for usuario in lista_run:
                    print(usuario) 
                print(lista_run)
            case 4:
                print("Esta es la ganancia obtenida por la venta de las entradas")
                print(f"La ganancia por la venta de entradas en total es de $ {sum(lista_ganancias)}") 
            case 5:
                print("Estas son las estadísticas de los rut que compraron entradas")
                print(f"El rut más alto que compró entrada es",max(lista_run)) 
                print(f"El rut más bajo que compró entrada es",min(lista_run)) 
            case 6:
                print("MUCHAS GRACIAS POR UTILIZAR NUESTRO SISTEMA")
                print("\t\t ADIÓS")
                break
            case 7:
                print("Cantidad de entradas vendidas por tipo:")
                for tipo, cantidad in entradas_vendidas.items():
                    print(f"{tipo}: {cantidad}")
            case 8:
                print("Cantidad de entradas compradas por cada usuario:")
                for usuario, cantidad in entradas_por_usuario.items():
                    print(f"Usuario {usuario}: {cantidad} entradas")
            case 9:
                usuario_mas_entradas = max(entradas_por_usuario, key=entradas_por_usuario.get)
                usuario_menos_entradas = min(entradas_por_usuario, key=entradas_por_usuario.get)
                print(f"Usuario que compró más entradas: {usuario_mas_entradas} con {entradas_por_usuario[usuario_mas_entradas]} entradas")
                print(f"Usuario que compró menos entradas: {usuario_menos_entradas} con {entradas_por_usuario[usuario_menos_entradas]} entradas")
            case 10:
                print("Ganancia por cada tipo de entrada:")
                for tipo, ganancia in ganancias_por_tipo.items():
                    print(f"{tipo}: ${ganancia}")
            case 11:
                asientos_vendidos = len([asiento for asiento in escenario if asiento == 0])
                asientos_no_vendidos = len([asiento for asiento in escenario if asiento != 0])
                print(f"Cantidad de asientos vendidos: {asientos_vendidos}")
                print(f"Cantidad de asientos no vendidos: {asientos_no_vendidos}")
