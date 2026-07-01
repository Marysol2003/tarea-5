#Semana 5
#Diferencia
#Implementa un algoritmo que calcule la diferencia entre dos conjuntos.
def diferencia_conjuntos(conjunto1, conjunto2):
    # Convertir los conjuntos a conjuntos de Python para facilitar la operación
    set1 = set(conjunto1)
    set2 = set(conjunto2)
    
    # Calcular la diferencia utilizando la operación de diferencia de conjuntos
    diferencia = set1 - set2
    
    # Convertir el resultado a una lista y devolverlo
    return list(diferencia)
print(diferencia_conjuntos([2, 4, 6, 8, 9], [1, 2, 6, 9]))  
print(diferencia_conjuntos([3, 2, 1, 4], [5, 6, 3, 4]))    
print(diferencia_conjuntos([1, 2, 3, 4], []))

#Diferencia simetrica
#Implementa programa que calcule la diferencia simetrica entre dos conjuntos. 
def diferencia_simetrica_directa(lista_a, lista_b):
    resultado = []
    union_temporal = lista_a + lista_b
    for elemento in union_temporal:
        if not (elemento in lista_a and elemento in lista_b):
            resultado.append(elemento)
    return resultado
print(diferencia_simetrica_directa([2, 4, 6, 8, 9], [1, 2, 6, 9]))

#Funciones anonimas
# Una lista con los precios base de diferentes productos
precios_base = [100, 250, 500, 1200]

# Usamos map() con una función lambda que multiplica por 1.16 y redondea a 2 decimales
precios_con_iva = list(map(lambda x: round(x * 1.16, 2), precios_base))

print(precios_con_iva)

#MIMAP
#Implementacion de mi_map 
def mi_map(funcion, lista):
    l=[]
    for elemento in lista:
        l = l + [funcion(elemento)]
    return l
#Definimos datos para ejemplo
#Registramos los capitales iniciales de diferentes inversiones
capitales_iniciales = [1000, 2500, 5000, 10000]
#Multiplicamos por 1.08 para simular rendimiento del 8%
capitales_proyectados = mi_map(lambda x: round(x * 1.08, 2), capitales_iniciales)
print("--- RESULTADOS DEL PROGRAMA MI_MAP ---")
print(f"Capitales iniciales:    {capitales_iniciales}")
print(f"Proyección (8% Rend.): {capitales_proyectados}")

#SELECCIONA
#Implementacion de selecciona y ejemplo de filtrado
def selecciona(lista, funcion_predicado):
    l = []
    for elemento in lista:
        if funcion_predicado(elemento):
            l = l + [elemento]
    return l
#Lista que representa los balances mensuales de una actividad
balances_mensuales = [1500, -320, 4800, -1250, 0, -95, 2300]
#Evalua si el balances es menos a 0
cuentas_con_perdidas = selecciona(balances_mensuales, lambda x: x < 0)
print("--- RESULTADOS DEL FILTRADO CON SELECCIONA ---")
print(f"Todos los balances registrados: {balances_mensuales}")
print(f"Balances con pérdidas (menores a 0): {cuentas_con_perdidas}")


#OCURRE
#Implementacion de ocurre y ejemplo de conteo
def ocurre(e, lista):
    conta = 0
    for elemento in lista: 
        if e == elemento:
            conta = conta + 1
    return conta
#Lista que representa las calificaciones obtenidas por un estudiante en diferentes exámenes
calificaciones = [9, 8, 10, 7, 9, 10, 8, 9, 6, 9]
nota_buscada = 9
total_ocurrencias = ocurre(nota_buscada, calificaciones)
print("--- RESULTADOS DEL CONTEO CON OCURRE ---")
print(f"Lista de calificaciones: {calificaciones}")
print(f"¿Cuántas veces aparece la nota {nota_buscada}?: {total_ocurrencias} veces")

#OCURREN
#Implementa un programa que determine las veces que ocurren los elementos de una lista. 
def ocurre(e, lista):
    conta = 0 
    for elemento in lista:
        if e == elemento:
            conta = conta + 1
    return conta
#lista de datos de control que contiene elementos repetidos
valores_medidos = [5, 3, 8, 5, 2, 3, 8, 5, 1]
valor_a_buscar = 5
total_repeticiones = ocurre(valor_a_buscar, valores_medidos)
print("--- EJECUCIÓN DEL ALGORITMO OCURRE ---")
print(f"Lista completa de valores: {valores_medidos}")
print(f"El número {valor_a_buscar} se repite un total de: {total_repeticiones} veces.")

#OCURREN
#Implementacion de OCURREN 
def ocurren(elementos_buscados, lista_principal):
    conta = 0 
    for elemento in lista_principal:
        if elemento in elementos_buscados:
            conta = conta + 1
    return conta
# Una lista con las categorías de los movimientos registrados en el mes
# (Donde: 'G' = Gasto, 'I' = Ingreso, 'I_F' = Ingreso Financiero, 'G_F' = Gasto Financiero)
historial_movimientos = ['G', 'I', 'G', 'G_F', 'I', 'G', 'I_F', 'G_F', 'I']

categorias_gasto = ['G', 'G_F']
total_gastos = ocurren(categorias_gasto, historial_movimientos)
print("--- RESULTADOS DEL ALGORITMO OCURREN ---")
print(f"Historial de movimientos:   {historial_movimientos}")
print(f"Categorías a contabilizar:  {categorias_gasto}")
print(f"Total de ocurrencias detectadas: {total_gastos}")

#ELIMNARREPETIDOS
#Eliminar elementos repetidos de una lista
def First(lista):
    return lista[0]

def Rest(lista):
    return lista[1:]

def elimina_repetidos(lista):
    L = []
    resto = Rest(lista)  
    
    for elemento in lista: 
        if elemento not in resto: 
            L = L + [elemento]
        
       
        resto = Rest(resto) 
        
    return L

# Pruebas
print(elimina_repetidos([1, 5, 3, 1, 2, 4, 2, 5]))  
print(elimina_repetidos([1, 1, 1, 1]))              
print(elimina_repetidos([]))

#Maximo
#Regresa el numero mayor de una lista de numeros.
def First(lista):
    return lista[0]
def maximo(lista):
    Max = First(lista)
    for elemento in lista:
        if Max < elemento:
            Max = elemento
    return Max  
print(maximo([10, 5, 3, 1]))
print(maximo([5, 20, 3, 1]))
print(maximo([5, 6, 23, 300]))