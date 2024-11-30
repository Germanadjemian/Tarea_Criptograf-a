import unicodedata
import numpy as np

# Función para contar caracteres en un texto.
def contar_caracteres(texto):
    """
    Calcula e imprime la cantidad de caracteres en el texto recibido.
    """
    # Calculamos el largo del texto usando len().
    largo = len(texto)
    # Imprimimos el resultado como un mensaje.
    print("Cantidad de caracteres: " + str(largo))

# Texto base para el análisis.
frase = "El esfuerzo y la dedicación son esenciales para alcanzar el éxito en cualquier campo profesional en la materia"
print("Frase: " + frase)
# Llamamos a la función para contar caracteres en la frase.
contar_caracteres(frase)

# Función para eliminar tildes de un texto.
def eliminar_tildes(texto):
    """
    Normaliza el texto eliminando tildes o caracteres especiales usando unicodedata.
    """
    # Normalizamos el texto a formato 'NFKD' para separar caracteres acentuados.
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    # Convertimos los caracteres acentuados a su forma base y eliminamos lo restante.
    return texto_normalizado.encode('ASCII', 'ignore').decode('ASCII')

# Función que convierte cada letra en un índice numérico según un alfabeto definido (el que se nos da en la tarea y aca representamos con la variable alafabeto).
def letra_numero(texto):
    """
    Convierte cada letra del texto en su índice correspondiente en nuestro alfabeto personalizado.
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyzñ *"  # Alfabeto con caracteres adicionales.
    lista = []
    texto = eliminar_tildes(texto)  # Eliminamos tildes para evitar errores.

    # Iteramos por cada letra en el texto transformado a minúsculas.
    for letra in texto.lower():
        # Verificamos si la letra está en el alfabeto.
        if letra in alfabeto:
            # Añadimos su índice numérico a la lista.
            lista.append(alfabeto.index(letra))
        else:
            # Si una letra no está en el alfabeto, devolvemos un mensaje de error.
            return "Error, ingrese una frase válida"
    return lista  # Retornamos la lista de índices.

# Función para encriptar texto con una fórmula matemática.
def encriptado_1(frase):
    """
    Aplicamos una fórmula matemática para encriptar el texto (la transformación lineal que nos da la letra con los valores de a y b que nostros elegimos):
    C = (5P + 10) mod 29, donde P es el índice de la letra en el alfabeto.
    """
    numeros = letra_numero(frase)  # Convertimos las letras a números ( a=0, b=1, c=2...).
    alfabeto = "abcdefghijklmnopqrstuvwxyzñ *"  # Alfabeto usado para encriptar.
    lista = []

    # Iteramos sobre cada número en la lista obtenida.
    for numero in numeros:
        # Aplicamos la fórmula de encriptación.
        imagen = (5 * numero + 10) % 29
        # Guardamos el resultado en la lista de números encriptados.
        lista.append(imagen)
    
    # Convertimos los números en letras usando el alfabeto.
    lista_2 = [alfabeto[numero] for numero in lista]
    # Retornamos el texto encriptado como una cadena.
    return "".join(lista_2)

# Función para encontrar la letra más repetida en un texto.
def letra_mas_repetida(texto):
    """
    Calcula qué letra aparece más veces en el texto
    """
    contador = {}  # Diccionario para contar ocurrencias de cada letra.

    # Iteramos por cada letra en el texto.
    for letra in texto:
        # Incrementamos el conteo de la letra en el diccionario.
        contador[letra] = contador.get(letra, 0) + 1

    # Encontramos la letra con la mayor frecuencia.
    letra_mas_frecuente = max(contador, key=contador.get)
    frecuencia = contador[letra_mas_frecuente]  # Obtenemos su frecuencia.
    if letra_mas_frecuente == " ":
        return "espacio_en_blanco", frecuencia
    return letra_mas_frecuente, frecuencia

# Función para encontrar las posiciones de una letra en una frase.
def posiciones_letra(frase, letra):
    """
    Encuentra todas las posiciones en las que aparece una letra específica en la frase.
    """
    # Usamos una comprensión de lista para obtener los índices donde aparece la letra.
    if letra == "espacio_en_blanco":
        letra = " "
    return [i for i, caracter in enumerate(frase) if caracter == letra]

# Mostramos los índices numéricos de cada letra de la frase.
print("Estos son los números correspondientes para cada letra de la frase (cada uno de estos representa P en la ecuación):")
print(letra_numero(frase))

# Encriptamos la frase y mostramos el resultado.
print("Al encriptar: '" + frase + "' obtengo:")
primera_encriptacion = encriptado_1(frase)
print(primera_encriptacion)

print()

# Encontramos la letra más repetida en la frase original y sus posiciones.
print("La letra que más se repetía en la frase original era:")
letra, frecuencia = letra_mas_repetida(frase)
print(f"Letra: {letra}, Frecuencia: {frecuencia}")
print("En las posiciones: " + str(posiciones_letra(frase, letra)))

# Encontramos la letra más repetida tras la encriptación y sus posiciones.
print("La letra que más se repite luego de encriptar la frase es:")
letra_enc, frecuencia_enc = letra_mas_repetida(primera_encriptacion)
print(f"Letra: {letra_enc}, Frecuencia: {frecuencia_enc}")
print("En las posiciones: " + str(posiciones_letra(primera_encriptacion, letra_enc)))

# Función para desencriptar texto.
def desencriptado_1(texto_encriptado):
    """
    Aplica la fórmula inversa para desencriptar:
    P = a^-1 * (C - b) mod 29, donde a^-1 es el inverso modular de 5.
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyzñ *"
    a_inverso = 6  # Inverso modular de 5 mod 29.
    b = 10
    lista = []

    # Iteramos sobre cada letra en el texto encriptado.
    for letra in texto_encriptado:
        # Obtenemos el índice numérico de la letra en el alfabeto.
        numero_encriptado = alfabeto.index(letra)
        # Aplicamos la fórmula de desencriptación.
        numero_original = (a_inverso * (numero_encriptado - b)) % 29
        # Convertimos el número de vuelta a una letra.
        lista.append(alfabeto[numero_original])
    
    # Retornamos el texto desencriptado como una cadena.
    return ''.join(lista)

# Desencriptamos y mostramos el texto original.
print("Desencriptando nos queda:")
print(desencriptado_1(primera_encriptacion))

# Generamos equivalencias entre caracteres originales y encriptados (para esto encriptamos el alfabeto original y sabemos que las letras resultantes seran la imagen correspondiente a cada letra).
alfabeto = "abcdefghijklmnopqrstuvwxyzñ *"
print("La encriptación de cada caracter del alfabeto corresponde a:")
alfabeto_encriptado = encriptado_1(alfabeto)
equivalencias = dict(zip(alfabeto, alfabeto_encriptado))
print(equivalencias.items())



print("")
print("SISTEMA CRIPTOGRÁFICO 2")
print("")


"""""Aca se nos complico mucho el tema de pasar las letra a numeros y viceversa (porque ya no era una frase entera sino cadenas de 3 constantemente, por lo que decidimos implementar nuevas funciones para esto)"""

# Función para dividir texto en bloques de longitud fija
def dividir_texto_longitud_fija_con_espacios(texto, longitud):
    # Aseguramos que el texto se puede dividir en bloques de longitud fija
    # Añadiendo espacios en blanco al final si es necesario
    while len(texto) % longitud != 0:
        texto += " "
    # Dividimos el texto en bloques de longitud especificada
    return [texto[i:i + longitud] for i in range(0, len(texto), longitud)]

# Función para convertir un carácter a su índice numérico en el alfabeto personalizado
def caracter_a_numero(caracter):
    # Tabla que asigna un número a cada letra del alfabeto y a caracteres especiales
    tabla = {
        **{chr(i + ord('a')): i for i in range(14)},  # a-n (0-13)
        "ñ": 14,
        **{chr(i + ord('o')): i + 15 for i in range(12)},  # o-z (15-26)
        " ": 27,  # El espacio se asigna al índice 27
        "*": 28  # El asterisco se asigna al índice 28
    }
    # Devuelve el índice numérico correspondiente al carácter o -1 si el carácter no está en la tabla
    return tabla.get(caracter.lower(), -1)

# Función para convertir un número en su correspondiente carácter en el alfabeto personalizado
def numero_a_caracter(numero):
    # Tabla que asigna un número a cada letra del alfabeto y a caracteres especiales
    tabla = {
        **{i: chr(i + ord('a')) for i in range(14)},  # 0-13 -> a-n
        14: "ñ",
        **{i + 15: chr(i + ord('o')) for i in range(12)},  # 15-26 -> o-z
        27: " ",  # El índice 27 corresponde al espacio
        28: "*"  # El índice 28 corresponde al asterisco
    }
    # Devuelve el carácter correspondiente al número o "?" si el número no está en la tabla
    return tabla.get(numero, "?")

# Función para convertir un texto en bloques numéricos
def bloques_a_vectores(texto, tamaño_bloque):
    # Aseguramos que el texto tiene longitud múltiplo del tamaño del bloque
    while len(texto) % tamaño_bloque != 0:
        texto += " "
    # Dividimos el texto en bloques
    bloques = [texto[i:i + tamaño_bloque] for i in range(0, len(texto), tamaño_bloque)]
    # Convertimos cada carácter de cada bloque a su índice numérico correspondiente
    vectores = [[caracter_a_numero(caracter) for caracter in bloque] for bloque in bloques]
    return vectores

# Función para convertir vectores encriptados en texto
def vectores_encriptados_a_texto(vectores_encriptados):
    resultado = ""
    # Convertimos cada número de los vectores en su correspondiente carácter
    for vector in vectores_encriptados:
        for num in vector:
            resultado += numero_a_caracter(num)
    return resultado

# Función de encriptado: realiza una transformación lineal sobre el vector de entrada
def funcion_encriptado_2(x, T, b):
    # Realiza el producto punto de la matriz T con el vector x, y le suma el vector b
    resultado = np.dot(T, x) + b
    # Devuelve el resultado módulo 29 (nuestro alfabeto tiene 29 caracteres)
    return np.mod(resultado, 29)

# Función para calcular la inversa modular de una matriz
def inversa_modular_matriz(matriz, modulo):
    # Calculamos el determinante de la matriz
    det = int(round(np.linalg.det(matriz)))  # Determinante
    # Calculamos la inversa modular del determinante
    det_inv = pow(det, -1, modulo)
    # Calculamos la matriz inversa modular y la devolvemos
    matriz_mod_inv = (det_inv * np.round(det * np.linalg.inv(matriz)).astype(int)) % modulo
    return matriz_mod_inv

# Función de desencriptado: deshace el proceso de encriptado
def funcion_desencriptado_2(y, T_inv, b, modulo):
    # Realiza el producto punto de la matriz T inversa con el vector (y - b)
    resultado = np.dot(T_inv, (y - b)) % modulo
    return resultado.astype(int)

# Datos iniciales para encriptar y desencriptar
texto = "El esfuerzo y la dedicacion son esenciales para alcanzar el exito en cualquier campo profesional en la materia"
longitud = 3  # La longitud de cada bloque de texto
modulo = 29  # El tamaño del alfabeto
T = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 7]])  # Matriz de transformación lineal
b = np.array([1, 2, 3])  # Vector de desplazamiento

# Dividimos el texto en bloques de longitud especificada
salida = dividir_texto_longitud_fija_con_espacios(texto, longitud)
# Convertimos el texto dividido en bloques a vectores numéricos
vectores = bloques_a_vectores(texto, longitud)

# Encriptación: aplicamos la función de encriptado a cada bloque
vectores_encriptados = []
for vector in vectores:
    vector_encriptado = funcion_encriptado_2(np.array(vector), T, b)
    vectores_encriptados.append(vector_encriptado)

# Convertimos los vectores encriptados en texto
mensaje_encriptado = vectores_encriptados_a_texto(vectores_encriptados)

# Desencriptado: calculamos la matriz inversa de T para deshacer el proceso
T_inv = inversa_modular_matriz(T, modulo)
# Aplicamos la función de desencriptado a cada bloque encriptado
vectores_desencriptados = []
for vector_encriptado in vectores_encriptados:
    vector_desencriptado = funcion_desencriptado_2(np.array(vector_encriptado), T_inv, b, modulo)
    vectores_desencriptados.append(vector_desencriptado)

# Convertimos los vectores desencriptados en texto
mensaje_desencriptado = vectores_encriptados_a_texto(vectores_desencriptados)

# Mostrar los resultados del proceso
print("Texto original:", texto)
print("\nBloques de texto:", salida)
print("\nVectores correspondientes:")
for vector in vectores:
    print(f"[{', '.join(map(str, vector))}]")
print("\nVectores encriptados:")
for vector in vectores_encriptados:
    print(f"[{', '.join(map(str, vector))}]")
print("\nMensaje encriptado:", mensaje_encriptado)
print("\nVectores desencriptados:")
for vector in vectores_desencriptados:
    print(f"[{', '.join(map(str, vector))}]")
print("\nTexto desencriptado:", mensaje_desencriptado)
