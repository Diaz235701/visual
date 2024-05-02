#valor de la compra y del color de la balota
valor_compra=float(input("Ingrese el valor de la compra: "))
color_balota=input("Ingrese el color de la balota(rojo,verde)")

decuento=0
#determino el descuento segun el color de la balota 
if color_balota=="rojo":
    descuento=valor_compra*0.15
elif color_balota=="verde":
    descuento=valor_compra*0.20
#calcular el valor a pagar 
    valor_a_pagar=valor_compra-descuento
#resultados 
print("valor de la compra:", valor_compra)
print("color de la balota:", color_balota)
print("descuento:", descuento)
print("valor a pagar:", valor_a_pagar)