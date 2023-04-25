# Operadores
#variable un espacio donde se guarda algo

#operador de suma / concatenacion || poner una variable junto a una caddena de caracteres

numero1 = 3
numero2 = 10

print(numero1 + numero2)

numero3 = "5"
numero4 = "10"

print(numero3 + numero4)

#operador de resta
print("------------RESTA-------------")
print(numero1 - numero2)
# esto no se puede hacer print(numero3 - numero4)



#operador de multiplicacion
print("------------MULTIPLICACION-------------")
print(numero1 * numero2)

#operador de DIVICION
print("------------DIVIVION-------------")
print(numero1 / numero2)
print(numero2 / numero1)

#operador de MODULO
#NOS DEVULVE EL RESIDIO DE UNA DIVICION ENTERA
print("------------MODULO-------------")
print(numero2 % numero1)

#operador de POTENCIA
#
print("------------POTENCIA-------------")
print(2 ** 3)
#PRINT(numero1 ** numero2)



#DIVICION ENTERA
#hace la divicion pero el resultado es entero, ignora cualquier decimal
print("------------DIVICION ENTERA-------------")
print(2 // 3)
print(numero2 // numero1)

#OPERADORES RELACIONALES
#MOYOR QUE 
print ("-------mayor que --------------")
#devulve trun si el numero de la izquierda es mayor al de la derecha
print (numero1 > numero2)

#MENOR  QUE 
print ("-------MENOR que --------------")

print (numero1 < numero2)

#operador de igualdad
print(" ---------IGUAL QUE ----------")
##da TRUE CUENDO SON IGUALES
#EN PYTHON NO EXITE LA IGUALDAD EXTRICTA
print (numero1 == numero2)
print (5 == 5)
print (5 == "5")
print (5 == 5.0 ) # DATOS FLOTANTES Y ENTEROS LOS TRATA COMO NUMERICOS


#OPERADOR MAYOR O IGUAL QUE 
print( "----------MAYOR O IGUAL QUE ------")

print(numero1 > numero1)
print(numero1 >= numero1)

#OPERADOR MAYOR O IGUAL QUE 
print( "----------MENOR O IGUAL QUE ------")

print(numero1 < numero1)
print(numero1 <= numero1)



#OPERADOR DE DESIGUALDAD
#NOS DA TRU SI AMBOS VALORES NO SON IGUALES
print( "----------MENOR O IGUAL QUE ------")

print (numero1 != numero2)
print (5 != 5)
print (5 != "5")
print (5 != 5.0 ) # DATOS FLOTANTES Y ENTEROS LOS TRATA COMO NUMERICOS


#OPERADORES AND BIT A BIT U OPERACION AND EN BINARIO
a = 2
b = 3
print("--------------and bit a bit----------")
print(a & b)

#OPERADORES OR BIT A BIT U OPERACION OR EN BINARIO
a = 2
b = 3
print("--------------OR bit a bit----------")
print(a | b)

#OPERADOR XOR BIT A BIT
print("--------------XOR bit a bit----------")
#si los dos son differente es un positivo
#si solo uno esta encendido con da verdadero
print (a ^ b)

#OPERADOR NOT BIT A BIT
print("--------------NOT bit a bit----------")
#INVERTIR CADA BIT EN EL OPERADOR
#OPERADOR DE UN SOLO NUMERO
"""~00000010 =2
11111111 = -2
= - 3 POR REGLA SE RESTA -1 = -$
""" 
print (~a) 
#desplazamiento a la derecha
print("DESPLAZAMIENTO A LA DERECHA")
"""00000010 este se recorre tres posiciones a las derecha 
00000011"""

print(a >> b)


#desplazamiento a la IZQUIERDA
print("DESPLAZAMIENTO A LA IZQUIERDA")
"""00000010 este se recorre tres posiciones a las derecha 
00000011"""

print(a << b)
print(b << a)

## OPERADORES LOGICOS

print("OPERADORES LOGICOS")

costo_cigarros = 50
dinero = 7
edad = 70
print(dinero >= costo_cigarros and edad >= 18)
print(True or False)

print("OPERADORES LOGICOS NOT")
### invierte la respuesta
costo_cigarros = 50
dinero = 7
edad = 70
print(not(dinero >= costo_cigarros and edad >= 18))
print(not(True or False))


### OPERADORES DE PERTENENCIA
print("OPERADORES DE PERTENENCIA in")
lista = [1, 2, 3, 4, 5]

## OPERADOR in
## te muestra TRUE si pertenece a una lista

print(3 in lista)
print(7 in lista)

print("OPERADORES DE PERTENENCIA not in")
lista = [1, 2, 3, 4, 5]

## OPERADOR in
## te muestra TRUE si pertenece a una lista

print(3 not in lista)
print(7 not in lista)


## operador de identidad
## sialgo esta en la misma ubicacion de memoria
print("operador de identidad IS")

a = 3
b = 3
c = 4
d = a

print(a is b)
print(a is d)
print(a is c)

print("operador de identidad IS not")
print(a is not b)
print(a is not d)
print(a is not c)

a = a + b

print(a)
print(b)


