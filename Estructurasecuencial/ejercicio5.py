#Declaramos las variables
valor_compra = float(input("Ingrese el valor de la compra: "))
descuento = float(input("Ingrese el valor del descuento: "))
#calculo el precio final
total_descuento=valor_compra*descuento
total_compra=valor_compra-descuento
#mensaje de todo el resultado de la compra con el descuento
print("La compra fue",valor_compra,"con un descuento de",descuento,"y el valor final a pagar es",total_compra)