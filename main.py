class Vehiculo:
    color = "Blanco"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 6000

auto = Coche

print(auto.color, auto.ruedas, auto.puertas, auto.velocidad, auto.cilindrada)
