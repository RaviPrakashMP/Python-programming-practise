#Using the starting and ending values of your car’s odometer,calculate its mileage

def MPG():
    print("The car's miles-per-gallon is",MilesPerGallon,"miles/gallon")

MilesDriven = float(input("Enter the number of miles driven"))
GallonsofGasUsed = float(input("Enter the gallons of gas used"))

MilesPerGallon = MilesDriven/GallonsofGasUsed

MPG()
