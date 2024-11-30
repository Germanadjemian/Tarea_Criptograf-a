import unicodedata

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
    Convierte cada letra del texto en su índice correspondiente en un alfabeto personalizado.
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
    numeros = letra_numero(frase)  # Convertimos las letras a números.
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
    Calcula qué letra aparece más veces en el texto, ignorando espacios y asteriscos.
    """
    contador = {}  # Diccionario para contar ocurrencias de cada letra.

    # Iteramos por cada letra en el texto.
    for letra in texto:
        if letra == " " or letra == "*":  # Ignoramos espacios y asteriscos.
            continue
        # Incrementamos el conteo de la letra en el diccionario.
        contador[letra] = contador.get(letra, 0) + 1

    # Encontramos la letra con la mayor frecuencia.
    letra_mas_frecuente = max(contador, key=contador.get)
    frecuencia = contador[letra_mas_frecuente]  # Obtenemos su frecuencia.
    return letra_mas_frecuente, frecuencia

# Función para encontrar las posiciones de una letra en una frase.
def posiciones_letra(frase, letra):
    """
    Encuentra todas las posiciones en las que aparece una letra específica en la frase.
    """
    # Usamos una comprensión de lista para obtener los índices donde aparece la letra.
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
