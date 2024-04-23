#declaramos variable
nombre_estudiante = str(input("Ingrese el nombre del estudiante: "))
calif_actividades = float(input("Ingrese la calificacion promedio de las actividades en clase: "))
calif_proyecto = float(input("Ingrese la calificacion del proyecto final"))
calif_evaluaciones = float(input("Ingrese la calificacion promedio de las evaluaciones"))
#calculo de las notas final
notas_final = (calif_actividades * 0.3) + (calif_proyecto * 0.5) + (calif_evaluaciones * 0.2)
#mensaje
print("La nota final de algoritmia del estudiante",nombre_estudiante,"es",notas_final)