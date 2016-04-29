#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

#Generar un numero aleatorio entre 1 y el 1000
x = random.randint(1,6);
print(str(x) + "\t");
print " "
print x

#Generar un numero aleatorio entre el 20 y el 30
x = random.randint(20,30)
print(str(x) + "\t");
print " "

#generar 50 numero aleatorios entre el 1 y el 100

for i in range(1,50):
	x = random.randint(1,100);
	print(str(x) + "\t")
print " "