import math

def sacando_definitiva(a , b):
    definitiva = (a*0.3)+(b*0.7)
    return definitiva

def buscando_nota(nota_deseada, primera_nota):
    resultado = ((nota_deseada - primera_nota * 0.3) / 0.7)
    return resultado

def redondear(numero):
    return math.ceil(numero * 10) / 10


while True:

    try:
        
        seleccione= int(input("\n Menú \n 1. Para la definitiva final de una materia (Te sabes las notas de los dos cortes).\n 2. Para saber que notas necesitas en el segundo corte para alcanzar la definitiva deseada(Te sabes solo la primera nota).\n 3. Para sacar el promedio, si no, para saber cuanto te falta. \n 0. Salir \n Seleccione: "))

        if (seleccione == 1):
            primer_corte = float(input("Definitiva primer corte: "))
            segundo_corte = float(input("Definitiva segundo corte: "))

            print("Tu definitiva final es de: ", redondear(sacando_definitiva(primer_corte, segundo_corte)))

        elif (seleccione == 2):    
            primer_corte = float(input("Definitiva primer corte: "))
            nota = float(input("Nota que quisieras sacar en definitiva: "))
            print("La nota que deberías sacar para el segundo corte es de: ", buscando_nota(nota, primer_corte))

        elif(seleccione == 3):
            prom_deseado = float(input("Ingrese su promedio deseado: "))
            num_materias = int(input("Ingrese su total de materias: "))

            notas=[]

            for i in range(num_materias):
                nota = float(input(f"Ingrese la nota de la materia {i+1}: "))
                notas.append(float(nota))

            materias_conocidas = [a for a in notas if a is not None]
            materia_faltantes = num_materias - len(materias_conocidas)

            if (materia_faltantes == 0):
                calc_promedio = sum(materias_conocidas) / num_materias
                print("El total de las notas han sido cargadas. tu promedio semestral es de: ", (redondear(calc_promedio)))
            else:
                suma_actual = sum(materias_conocidas)
                nota_necesaria_total = prom_deseado * num_materias
                nota_faltante_total = nota_necesaria_total - suma_actual
                nota_necesaria_por_materia = nota_faltante_total / materia_faltantes

                print(f"Debes sacar en promedio {nota_necesaria_por_materia:.2f} en las {materia_faltantes} materias restantes para lograr un promedio de {prom_deseado}.")

        elif(seleccione == 0):    
            print("The software say: Bye :')")
            break

        else:
            print("La opción que escogió no exite, vuelvalo a intentar")

    except ValueError:
        print("Por favor ingrese un valor valido")





