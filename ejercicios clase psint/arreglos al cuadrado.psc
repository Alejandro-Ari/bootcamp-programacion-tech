Proceso arreglos2
	Escribir "ingresa la cantidad de números a elevar"
	Leer n
	Dimension numeros[n]
	Dimension cuadrados[n]
	Para i = 0 Hasta  n -1 Hacer
		Escribir "Ingresa el valor"
		Escribir i
		Leer numeros[i]
		cuadrados[i] = numeros[i] * numeros[i]
		Escribir "elevado al cuadro es : ", cuadrados[i]
		
	FinPara
	
	
FinProceso
