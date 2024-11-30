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
    alfabeto = "abcdefghijklmnopqrstuvwxyzñ *"
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
    alfabeto = "abcdefghijklmnopqrstuvwxyzñ *"
    lista = []
    lista_2 = []
    for numero in numeros:
        imagen= (5 * numero + 10) % 29 #Aplico el algoritmo de encriptado
        lista.append(imagen)
   
    for numero in lista:
        lista_2.append(alfabeto[numero])#Para cada numero/imagen saliente del algoritmo agarro su equivalente en la tabla de conversión de letras a números pero al reves, esta vez de número a letra.
    resultado = "".join(lista_2)
    return resultado

def letra_mas_repetida(texto):#Devuelve la letra más repetida y también las veces que esta se repite
    contador = {}  # Diccionario para contar las letras y los espacios
    
    for letra in texto:
        if letra == " " or letra == "*": #Los esapcios en blanco y asteriscos no son letras, por lo que no los contamos
            continue
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    
    # Encontrar la letra o el espacio con la máxima frecuencia
    letra_mas_frecuente = max(contador, key=contador.get)
    frecuencia = contador[letra_mas_frecuente]
    return letra_mas_frecuente, frecuencia

def posiciones_letra(frase, letra):
    lista = []
    cont= 0
    for caracter in frase:
        if caracter == letra:
            lista.append(cont)
        cont+=1
    return lista



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
print("En las posiciones: " + str(posiciones_letra(frase, letra_mas_repetida(frase)[0])))

#En un principio cambiaría la letra más repetida por su imagen correspondiente, pero manteniendo el número de veces que se repite y las posiciones. No obstante al no incluir los espacios (ni asteriscos) a la hora de contar la letra que más se repite, en el primero nos da que es "a" con 14 y en el segundo a con 17, este a con 17 son los espacios en blanco, presentes 17 veces en el texto, pero que anteriormente no los contaba porque no son una letra, pero como su imagen tras encriptar es a para todos, ahora si se cuentan.

print("La letra que más se repite luego de encriptada la frase es:")
print(letra_mas_repetida(primera_encriptacion))
print("En las posiciones: " + str(posiciones_letra(primera_encriptacion, letra_mas_repetida(primera_encriptacion)[0])))

def desencriptado_1(texto_encriptado):
    alfabeto = "abcdefghijklmnopqrstuvwxyzñ *"
    # Inverso de 'a' en módulo 29 (a=5, a^-1=6)
    a_inverso = 6
    b = 10 #definimos a_inverso y b para que en caso de elegir otros valores para a y b en un mismo planteo, este codigo pueda ser reutilizado simplemente sustituyendo sus respectivos valores
    lista = []
    #Como la cadena ya esta sanitizada al encriptarlo no necesito volver a hacerlo
    for letra in texto_encriptado:
        numero_encriptado = alfabeto.index(letra)
        # Desencriptamos con la fórmula P = a^-1 * (C - b) % 29
        numero_original = (a_inverso * (numero_encriptado - b)) % 29
        lista.append(alfabeto[numero_original])
    
    # Devolvemos el texto desencriptado
    return ''.join(lista)

print("Desencriptando nos queda:")
print(desencriptado_1(primera_encriptacion))


alfabeto = "abcdefghijklmnopqrstuvwxyzñ *"
print("La encriptación de cada caracter del alfabeto '" +alfabeto+"' corresponden respectivamente a cada una de las siguientes letras: ")
alfabeto_encriptado = encriptado_1(alfabeto)
alfabeto = list(alfabeto)
alfabeto_encriptado = list(alfabeto_encriptado)
equivalencias = dict(zip(alfabeto, alfabeto_encriptado))
print(equivalencias.items())