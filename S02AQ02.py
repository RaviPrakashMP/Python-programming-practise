def fuel_consumed():
    print("The amount of GallonsofGasUsed is",GallonsofGasUsed)
    
NOD_OOD = float(input("The distance travelled:"))

mileage = float(input("The mileage of car is:"))

GallonsofGasUsed = NOD_OOD/mileage

fuel_consumed()

def fuel_refill():
    print("The number of times car stopped to fill the fuel tank is",Stops)

Tankcapacity = float(input("The amount of fuel a tank can hold:"))

Stops = GallonsofGasUsed // Tankcapacity

fuel_refill()
