# ##adivinar numero
# import random



# numeroAadivinar=random.randint(1,50)

# num=int(input("Adivine el numero" ))

# while num!=numeroAadivinar:
#     if num>numeroAadivinar:
#         print("El numero a adivinar es menor")
#     else:
#         print("El numero a adivinar es mayor")
#     num=int(input("Adivine el numero"))
#     print("Le achuntaste! ")

arancel=200000
descuento=0

print('''
      1.- La florida 20%
      2.- La Pintana 30%
      3.- Puente Alto 25%
      4.- san joaquin 15%
      ''')
comuna=int(input("seleccione una comuna"))
if comuna==1:
    descuento=20
elif comuna==2:
    descuento=30
elif comuna==3:
    descuento=25
elif comuna==4:
    descuento==15
else:
    print("seleccion incorrecta")

grupo=int(input("ingrese su grupo familiar(numero entero usted incluido):"))
if grupo==1:
    descuento+=2
elif grupo<=4 and grupo>=2:
    descuento+=3
elif comuna>5:
    descuento+4
else:
    print("seleccion incorrecta")
    print("El descuento total es", descuento)
    desc=arancel*descuento/100
    total=arancel-descuento
    print("El total a pagas es $",total)
          



                 


                      