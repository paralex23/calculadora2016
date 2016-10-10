Feature: suma de dos numeros
	Yo como usuario de la calculadora deseo 
	realizar una suma de dos numeros para poder
	tener un resultado confiable

 Scenario: sumar 2 mas 2
	Dado que tengo los operadores "2" y "2"
	cuando realizo la suma
	entonces el resultado que obtego es "4"

 Scenario: sumar 5 mas 5
	Dado que tengo los operadores "5" y "5"
	cuando realizo la suma
	entonces el resultado que obtego es "10"

 Scenario: sumar 20 mas 1
	Dado que tengo los operadores "20" y "1"
	cuando realizo la suma
	entonces el resultado que obtego es "21"