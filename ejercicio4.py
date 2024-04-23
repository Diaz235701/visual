#Declaracion variables
sueldo=2000000
total_comosiciones=0
comisiones=300
ventas=0
total= 0

nombre=str(input("Nombre del vendedor"))
ventas=int(input("digite la cantidad de la venta"))

total_comosiciones=ventas*comisiones
total_sueldo=total_comosiciones+sueldo

print("El vendedor",nombre,"tiene un sueldo de",sueldo,"durante el mes obtuvo una comision de",total_comosiciones,"y el valor final a pagar es",total_sueldo)
