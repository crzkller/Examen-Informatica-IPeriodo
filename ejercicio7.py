
print("Convertidor de tiempo")
print("1 - Segundos a Minutos \n2 - Segundos a Horas")
opcion = int(input("Qué opción de conversión desea utilizar: "))
resultado = 0
 
if opcion == 1:
    print("Segundos a Minutos")
    entrada = float(input("Escribe la cantidad en Segundos: "))
    resultado = round(entrada/60)
elif opcion == 2:
    print("Segundos a Horas")
    entrada = float(input("Escribe la cantidad en Segundos: "))
    resultado = round(entrada/3600)
 
print("El resultado es: {} ".format(resultado))
