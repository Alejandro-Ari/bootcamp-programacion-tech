
tu_dinero = int(input("cuanto traes?"))

edad = 20
cover = 100

costo_vip = 500
print("Edad: ", edad)
if edad >= 18 and tu_dinero >= cover:
    tu_dinero = tu_dinero - cover
    print("pasale")
    print("¿quieres un cigarro?")
    print("Ahora tienes: ", tu_dinero)
    if tu_dinero >= costo_vip:
        tu_dinero = tu_dinero - cover

        print("Pasale al VIP")
        print("Ahora tienes: ", tu_dinero)
    else:
        print("tu no puedes pasar al vip , cuesta 500")