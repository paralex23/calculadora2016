# -*- coding: utf-8 -*-
from lettuce import step, world
from Calculadora import Calculadora

@step(u'Dado que tengo los operadores "([^"]*)" y "([^"]*)"')
def dado_que_tengo_los_operadores_group1_y_group1(step, num1, num2):
	cal  = Calculadora()
	world.resultado = cal.suma (int (num1), int (num2))
    
@step(u'cuando realizo la suma')
def cuando_realizo_la_suma(step):
	pass 
    
@step(u'entonces el resultado que obtego es "([^"]*)"')
def entonces_el_resultado_que_obtego_es_group1(step, esperado):
    assert int (esperado) == world.resultado, 'El resultado no es el mismo'
