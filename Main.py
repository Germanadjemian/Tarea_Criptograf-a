import unicodedata

#Función para contar que tenga los 100 caracteres, lo imprime para visualizarlo.
def contar_caracteres(texto):
    largo= len(texto)
    print("Cantidad de caracteres: "+ str(largo))

frase = "El esfuerzo y la dedicación son esenciales para alcanzar el éxito en cualquier campo profesional en la materia"
print("Frase: "+frase)
contar_caracteres(frase)#Da 110 caracateres

#Funcion para eliminar tildes
def eliminar_tildes(texto):
    """Elimina tildes de una cadena utilizando unicodedata.

    Args:
        texto: La cadena de entrada.

    Returns:
        La cadena sin tildes.
    """

    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

#Funcion para convertir las letras a su respectivo número
def letra_numero(texto):
    alfabeto = "abcdefghijklmnopqrstuvwxyzñ "
    lista= []
    texto = eliminar_tildes(texto)
    
    for letra in texto:
        letra = letra.lower()
        if letra in alfabeto:
            lista.append(alfabeto.index(letra))
        else:
            return "Error, ingrese una frase valida"
    return lista #devuelve lista de enteros
        
    
#Funcion de encriptado (elegeimos a= 5 y b= 10)
def encriptado_1(frase):
    numeros = letra_numero(frase) #Convierto a=0, b=1, c=2.....
    alfabeto = "abcdefghijklmnopqrstuvwxyzñ "
    lista = []
    lista_2 = []
    for numero in numeros:
        imagen= (5 * numero + 10) % 29 #Aplico el algoritmo de encriptado
        lista.append(imagen)
    #resultado = ''.join(map(str, lista)) #devuelvo una sola cadena uniendo toda la lista
    for numero in lista:
        lista_2.append(alfabeto[numero])
    resultado = "".join(lista_2)
    return resultado

def letra_mas_repetida(texto):
    contador = {}  # Diccionario para contar las letras y los espacios
    
    for letra in texto:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    
    # Encontrar la letra o el espacio con la máxima frecuencia
    letra_mas_frecuente = max(contador, key=contador.get)
    frecuencia = contador[letra_mas_frecuente]
    return letra_mas_frecuente, frecuencia

#Resultado de la concersión entre letras y números
print("Estos son los números correspondientes para cada letra de la frase, de la primera a la última:")
print(letra_numero(frase))

#Resultado del primero encriptado
print("Al encriptar: '"+frase+"' obtengo:")
primera_encriptacion = encriptado_1(frase)
print(primera_encriptacion)

print()

print("La letra que más se repetía en la frase original era:")
print(letra_mas_repetida(frase))
print("La letra que más se repite luego de encriptada la frase es:")
print(letra_mas_repetida(primera_encriptacion))

