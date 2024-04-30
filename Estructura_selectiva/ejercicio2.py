cantidadd_zapatillas = int(input("Ingrese la cantidad de la zapatilla:"))
precio_zapatilla = float(input("Ingrese el precio de la zapatilla:"))

total_sin_descuento = cantidadd_zapatillas * precio_zapatilla

if cantidadd_zapatillas >=3:
   descuento = total_sin_descuento * 0.20
else:
   descuento = total_sin_descuento * 0.10

total_a_pagar = total_sin_descuento - descuento

print("Total a pagar es:", total_a_pagar)