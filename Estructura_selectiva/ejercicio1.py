#defino las tres calificaciones del aprendiz
Calificacion1 = float(input("Ingrese la primera calificacion"))
Calificacion2 = float(input("Ingrese la segunda calificacion"))
Calificacion3 = float(input("Ingrese la tercera calificacion"))
#calculo del promedio de las calificaciones
promedio = (Calificacion1+Calificacion2+Calificacion3) /3
#determino si el aprendiz aprueba o desaprueba algoritmia con condiciones explicitas
if promedio  >=70:
   print("El aprendiz aprobo algoritmia con un promedio de", promedio)
#resultado
else:
   print("El aprendiz desaprobo algoritmia con un promedio de", promedio)
