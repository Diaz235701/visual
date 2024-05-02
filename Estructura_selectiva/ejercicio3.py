#monto total de la compra
monto_total_compra = int(input("Digite el monto total de la compra:"))
#determino como la empresa pagara al fabricante segun el monto total de la compra
if monto_total_compra > 500000: 
     dinero = monto_total_compra*0.55
     prestamo = monto_total_compra * 0.30 
     credito_fabricante = monto_total_compra * 0.15+(monto_total_compra*0.20)

else: 
    dinero = monto_total_compra * 0.70
    credito_fabricante = monto_total_compra*0.30+(monto_total_compra*0.20)
    prestamo = 0
#cacular los interes del credito al fabricante
intereses_credito_fabricante = credito_fabricante*0.20

#resultado
print("Valor invertido por su propio dinero:", dinero)
print("valor prestamo:", prestamo)
print("Valor del credito solicitado al fabricante:",credito_fabricante)
print("Intereses del credito al fabricante:",intereses_credito_fabricante)