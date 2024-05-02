#defino las funciones (hemoglobina en las personas,edaad de la persona y el sexo de la persona)
nombre_paciente=input("Ingrese su nombre:")
edad=float(input("Ingrese la edad:"))
sexo=input("Ingrese el sexo M O F:")
nivel_hemoglobina=float(input("Ingrese el nivel de hemoglobina en g%: "))

#aclaramos si el nivel de hemoglobina es mayor o meno a 0
tiene_anemia = False
#aqui determinamos el resultado como positivo y en caso contrario negativo 
if edad <=1/12:
    if nivel_hemoglobina < 13 or nivel_hemoglobina>26:
     tiene_anemia = True
elif 1/12 < edad <= 6/12:
    if nivel_hemoglobina < 10 or nivel_hemoglobina > 18:
     tiene_anemia = True
elif 6/12 < edad <= 12/12:
    if nivel_hemoglobina < 11 or nivel_hemoglobina > 15:
     tiene_anemia = True
elif 1 < edad <= 5:
    if nivel_hemoglobina < 11.5 or nivel_hemoglobina > 15:
     tiene_anemia = True
elif 5 < edad <= 10:
    if nivel_hemoglobina < 12.6 or nivel_hemoglobina > 15.5:
      tiene_anemia = True
elif 5 < edad <= 15:
    if nivel_hemoglobina < 13 or nivel_hemoglobina > 15.5:
     tiene_anemia = True 
elif sexo == "M" and edad > 15:
    if nivel_hemoglobina < 12 or nivel_hemoglobina > 16:
     tiene_anemia = True 
elif sexo == "H" and edad > 15:
    if nivel_hemoglobina < 14 or nivel_hemoglobina > 18:
     tiene_anemia = True 
#resultado final si tiene o no anemia 
if tiene_anemia:
   print("El resultado es: Positivo anemia ")
else:
   print("El resultado: Negativo anemia")
