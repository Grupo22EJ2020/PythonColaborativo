from alexaSherlyn import AlexaSherlyn
from bryan20nietosi import Bryan20nietosi
from emichics import Emichics
from t0biaslj import T0biaslj
from DanielRojas2002 import danielRojas2002
print("Bienvenido al programa")
print("Personas de la organizacion")
print("1.-Pasatiempos de Liigabriel")
print("2.-Pasatiempos de bryan20nietosi")
print("3.-Pasatiempos otro alumno (lo ayude)")
print("4.-Pasatiempos de Orlando190")
print("5.-Pasatiempos de aldo1871")
print("6.-Pasatiempos de ArcelLopez11")
print("7.-Pasatiempo de Apolion44")
print("8-Pasatiempos de DanielRojas2002")
print("9.-Pasatiempos de T0biasLJ")
print("10.-Pasatiempos de MayteRivera22")
print("11.-Pasatiempos de Yaressildiaz1101")
print("12.-Pasatiempos de LilianaGR")
print("13.-Pasatiempos de AlexaSherlyn")
print("14.-Pasatiempos de Emichics ")
opcion = int(input("Que opcion eliges: "))
if opcion == 1:
    print("Eligio el miembro 1")
elif opcion == 2: 
    muestra= Bryan20nietosi()
    muestra.PasatiemposBryan()
elif opcion == 3:
    print("Eligio otro alumno")
elif opcion == 4:
    print("Eligio el miembro 4")
elif opcion == 5:
    print("Eligo el miembro 5")
elif opcion == 6:
    print("Eligio el miembro 6")
elif opcion == 7: 
    print("Eligio el miembro 7")
elif opcion == 8: 
    Info=danielRojas2002()
    Info.ImprimirPasatiempo()
elif opcion == 9:
    info= T0biaslj
    info.mispasatiempos
elif opcion == 10:
    print("Eligio el miembro 10")
elif opcion == 11:
    print("Eligio el miembro 11")
elif opcion == 12:
    print("Eligio el miembro 12")
elif opcion == 13:
    yo = AlexaSherlyn()
    yo.imprimirPasatiempos()
elif opcion == 14:
    objeto = Emichics()
    objeto.imprimirHobbies()

