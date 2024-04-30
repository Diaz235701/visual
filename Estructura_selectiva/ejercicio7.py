cantidad_llantas=int(input("Ingrese la cantidad de llantas compradas: "))

if cantidad_llantas <5:
    precio_por_llanta=300
elif cantidad_llantas>=5 and cantidad_llantas <=10:
    precio_por_llanta=250
else:
    precio_por_llanta=200

monto_total=cantidad_llantas*precio_por_llanta

print("Cantidad de llantas compradas:", cantidad_llantas)
print("Precio por llantas:",precio_por_llanta)
print("Monto total a pagar:", monto_total)