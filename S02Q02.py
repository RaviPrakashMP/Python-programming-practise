NOD_OOD = float(input("The distance travelled:"))

mileage = float(input("The mileage of car is:"))

GallonsofGasUsed = NOD_OOD/mileage

print("The amount of GallonsofGasUsed is",GallonsofGasUsed)

Tankcapacity = float(input("The amount of fuel a tank can hold:"))

Stops = GallonsofGasUsed // Tankcapacity

print("The number of times car stopped to fill the fuel tank is",Stops)
