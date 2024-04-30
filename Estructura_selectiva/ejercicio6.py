promedio=float(input("Digite el promedio obtenido en el ultimo periodo:"))

if promedio >=9:
    descuento=0.30 
    monto_a_pagar=(1-descuento)* 100
else:
    descuento=0
    monto_a_pagar=100

    if promedio <9:
        monto_a_pagar *=1.10

print("El monto a pagar es:", monto_a_pagar)