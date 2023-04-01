# Tipos de datos
dato = "5" # una cadena de carateres o string o cadena de texto, por las comillas
print (dato + dato) #esto es una concatenación, porque son string
dato = 5 #númerico - Entero sin decimales
print (dato + dato) # esto si es una suma porque son datos numericos
dato = 5.0 # es un dato numero pero es flotante (porque puede que esl flotante 
#flote entre dos numeros enteros) - con punto decimal
print (dato + dato)
dato = True #Booleano - puede ser verdadero o falso
print (dato + dato)
dato = False #Booleano - puede ser verdadero o falso
print (dato + dato)

"""


cinco ="5"
numero = 5
print (cinco + numero)


Traceback (most recent call last):
  line 16, in <module>  
    print (cinco + numero)
           ~~~~~~^~~~~~~~
TypeError: can only concatenate str (not "int") to str

"""
"""
Exiten erores en sintaxis, en tiempo de ejecución 
"""
#para que funcione el codigo de arriba
#solucion 1: convertir el valor

cinco ="5"
numero = 5

##castear o pastear}
#parsar: de un tipo de dato string a int
#string a flotante

numero_string = str(numero)
print (cinco + numero_string)


#################

cinco ="5"
numero = 5

numero_string = int(cinco)
print (numero + numero_string)


cinco ="5"
numero = 5


print (float(cinco) + numero)


#Solución 2 : Formato de cadenas

nombre = "alejandro"
edad = 27
#el obajetivo es imprimir: HOLA MI NOMBRE ES ALEJANDRO Y TENGO 27 AÑOS


"""
print ("HOLA MI NOMBRE ES" + nombre + "Y TENGO" + edad + "AÑOS")

   print ("HOLA MI NOMBRE ES" + nombre + "Y TENGO" + edad + "AÑOS")
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
TypeError: can only concatenate str (not "int") to str
"""
#aplicando formato de cadenas: donde queramos meter la variable le ponemos llaves
#string tiene funciones al interior y una de ellas es .format

print ("HOLA MI NOMBRE ES {} y TENGO {} AÑOS".format(nombre, edad))

#solucion 3: f-string

print (f"HOLA MI NOMBRE ES {nombre} y TENGO {edad} AÑOS")

#solucion 1 de nuevo: cast del dato  - con concatenacion
print ("HOLA MI NOMBRE ES " + nombre + " y TENGO " + str(edad) + " AÑOS")


print (__name__)

## la funcion exit cierra el programa de python
# exit()