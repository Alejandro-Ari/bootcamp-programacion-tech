Proceso comprobador
	Escribir 'Dame tu edad'
	Leer edad
	Si edad>=18 Y edad<=130 Entonces
		Escribir 'Pasale '
	SiNo
		Si edad<0 O edad>130 Entonces
			Escribir 'No deberias existir'
		SiNo
			Si edad<18 Entonces
				Escribir 'Estas muy chico'
			FinSi
		FinSi
	FinSi
FinProceso
