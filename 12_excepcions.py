
numerOne = 5
numbertwo = 1
numbertwo ="2"

try:
    print(numbertwo + numerOne)
except:
    print("Se ha producido un error")
else: 
    print("La ejecucion continúa correctamente")
finally:
    print("La ejecucion continua")



try:
    print(numbertwo + numerOne)
except Exception as error:
    print(error)

else: 
    print("La ejecucion continúa correctamente")