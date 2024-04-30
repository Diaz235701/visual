sexo=input("Ingrese el sexo(F o M):")
edad=int(input("Ingrese la edad de la persona:"))


if sexo=="F":
    num_pulsaciones=(200-edad)/10
elif sexo=="M":
     num_pulsaciones=(210-edad)/10
else:
    print("Sexo no valido. Por favor ingrese 'F' O 'M'.")
    
    print("El numero de las pulsaciones por cada 10 segundos de ejercicio arobicos es de:", num_pulsaciones)