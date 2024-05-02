#promedio obtenido por el alumno 
promedio=float(input("Digite el promedio obtenido en el ultimo periodo:"))
#calculamos el descuento y del monto a pagar 
if promedio >=9:
    descuento=0.30 
    monto_a_pagar=(1-descuento)* 100
else:
    descuento=0
    monto_a_pagar=100
#si el promedio es menor que 9,se agrega el 10% de IVA
    if promedio <9:
        monto_a_pagar *1.10
#imprime el monto a pagar 
print("El monto a pagar es:", monto_a_pagar)