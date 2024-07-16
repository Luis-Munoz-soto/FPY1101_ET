#examen transversal

#nota profesor no pude lograr abrir las funciones, trabaje practicamente a siegas

import random
import csv
op = 0

trabajadores = ["Juan Peres",
                "Maria Garcia",
                "Carlos Lopez",
                "Ana Martinez",
                "Pedro Rodriguez",
                "Laura Hernandez",
                "Miguel Sanchez",
                "Isabel Gomez",
                "Francisco Dias",
                "Elena Hernandez"
                ]

reportesueldos =[]

#funcion para asignar sueldos
def asignar_sueldo():
      sueldo = random(300000, 2500000)

      trabajadores.append({
            "Juan Peres": sueldo,
            "Maria Garcia":sueldo,
            "Carlos Lopez": sueldo,
            "Ana Martinez": sueldo,
            "Pedro Rodriguez": sueldo,
            "Laura Hernandez": sueldo ,
            "Miguel Sanchez": sueldo,
            "Isabel Gomez": sueldo,
            "Francisco Dias": sueldo,
            "Elena Hernandez": sueldo
      })


      for trabajador in trabajadores:
         print(trabajadores)

#funcion para ver sueldo minimo
def sueldo_minimo():
      for i in range(1, len(trabajadores)):
            if trabajadores[i] < minimo:
                  minimo = trabajadores[i]
    
            return(minimo)

#funcion para ver sueldo mayor
def sueldo_mayor():
      for i in range(1, len(trabajadores)):
            if trabajadores[i] > mayor:
                  mayor = trabajadores[i]
            return(mayor)

#funcion para ver promedio
def promedio_sueldos():
      promedio= sum(trabajadores)/len(trabajadores)

      return(promedio)

#fncion para calificar sueldos
def calificar_sueldo():
      if trabajadores >= 800000:
            for trabajadores in len(trabajadores):
                  trabajadores_menor=[]
                  trabajadores_menor.append({
                        "Nombre trabajador": trabajadores,
                        "Sueldo trabajador": sueldo_minimo
                        })
                  return(trabajadores_menor)

      elif trabajadores == 800000:
            for trabajadores in len (trabajadores):
                  trabajadores_promedio = []
                  trabajadores_promedio.append({
                        "Nombre trabajador": trabajadores,
                        "Sueldo trabajador": promedio_sueldos
                        })
                  return(trabajadores_promedio)

      elif trabajadores <= 2000000:
            for trabajadores in len(trabajadores):
                  trabajadores_mayor = []
                  trabajadores_mayor.append({
                        "Nombre trabajador": trabajadores,
                        "Sueldo trabajador": sueldo_mayor
                        })
                  return(trabajadores_mayor)

 #funcion para estadisticas de sueldos                 
def ver_estadisticas():
      
      sueldo_mas_alto = print("El sueldo mas alto es: $")
      sueldo_mas_bajo = print("El sueldo mas bajo es: $")
      promedio_de_sueldos = print("El promedio de los sueldos es: $")
      media_aritmetica = print("La media aritmetica de los sueldos es: $")

#funcion para reporte de sueldos
def reporte_sueldo():
      
      sueldo_base = trabajadores
      descuento_salud = trabajadores * 0.07
      descuento_afp = trabajadores * 0.12
      sueldo_liquido = trabajadores - descuento_afp - descuento_salud

      reportesueldos.append({
            "Nombre trabajador": trabajadores,
            "Sueldo base": sueldo_base,
            "Descuento salud": descuento_salud,
            "Descuento AFP": descuento_afp,
            "Sueldo liquido": sueldo_liquido
      })


#menu principal
while True:
    print("-"*40)
    print("======MENU=======")
    print("-"*40)
    print("1. Asignar sueldos aleatorios")
    print("2. Clificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    while True:
                try:
                    op = int(input("Que opcion deceas realizar: "))
                    if op >= 1 and op <= 5:
                        break
                    else:
                        print("")
                        print("Opcion incorrecta, esta debe ser entre 1 y 5")
                        print("")
                except ValueError:
                    print("")
                    print("Opcion incorrecta, esta debe ser entre 1 y 5")
                    print("")

    if op == 1:
          print("1")
    elif op == 2:
          print("2")
    elif op == 3:
          print("3")
    elif op == 4:
          print("4")
    elif op == 5:
          break

print("")  
print("fin del programa")
print("Desarrollado por: Luis Muñoz")
print("RUT: 19.114.545-3")